# -*- coding: utf-8 -*-

import time
import threading
from turtle import Turtle
from typing import Tuple
from hamcrest import instance_of
from watchdog.observers import Observer
from watchdog.events import *
from watchdog.utils.dirsnapshot import DirectorySnapshot, DirectorySnapshotDiff
from mdinfo import MDInfo


class FileEventHandler(FileSystemEventHandler):
    def __init__(self, aim_path, info_observer: MDInfo):
        FileSystemEventHandler.__init__(self)
        self.aim_path = aim_path
        self.timer = None
        self.snapshot = DirectorySnapshot(self.aim_path)
        self.info_observer = info_observer

    def on_any_event(self, event):
        if self.timer:
            self.timer.cancel()

        self.timer = threading.Timer(0.2, self.checkSnapshot)
        self.timer.start()

    def checkSnapshot(self):
        snapshot = DirectorySnapshot(self.aim_path)
        diff = DirectorySnapshotDiff(self.snapshot, snapshot)
        self.snapshot = snapshot
        self.timer = None

        diff_file = set()

        diff_file.update(diff.files_created,
                         diff.files_deleted,
                         diff.files_modified,
                         diff.files_moved)

        for file in diff_file:
            if isinstance(file, Tuple):
                if file[0].endswith(".md"):
                    self.info_observer.remove_info(file[0])
                if file[1].endswith(".md"):
                    self.info_observer.add_info(file[1])
            else:
                self.info_observer.renew_file(file)

        # self.info_observer.renew_files(files)
        # print(file)

        # print("files_created:", diff.files_created)
        # print("files_deleted:", diff.files_deleted)
        # print("files_modified:", diff.files_modified)
        # print("files_moved:", diff.files_moved)
        # print("dirs_modified:", diff.dirs_modified)
        # print("dirs_moved:", diff.dirs_moved)
        # print("dirs_deleted:", diff.dirs_deleted)
        # print("dirs_created:", diff.dirs_created)


class DirMonitor(object):
    def __init__(self, aim_path, info_observer: MDInfo):
        self.info_observer = info_observer
        self.aim_path = aim_path
        self.observer = Observer()

    def start(self):
        event_handler = FileEventHandler(self.aim_path, self.info_observer)
        self.observer.schedule(event_handler, self.aim_path, True)
        self.observer.start()

    def stop(self):
        self.observer.stop()


if __name__ == "__main__":
    monitor = DirMonitor(r"md")
    monitor.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        monitor.stop()
        monitor.join()
