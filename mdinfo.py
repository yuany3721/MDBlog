# -*- coding:utf-8 -*-

import os
import re

from importlib_metadata import Deprecated
from numpy import deprecate


class MDInfo:
    md_meta = {}    # 存放md文档元数据
    tags = {}       # 存放文档tags

    def __init__(self):
        self.read_dir("md")
        for filename in self.md_meta.keys():
            for t in self.md_meta[filename]["tags"]:
                if t in self.tags.keys():
                    self.tags[t].append(filename)
                else:
                    self.tags[t] = [filename]

    def read_dir(self, path):
        # 读取path下所有md文件并放入元数据数组中
        for file in os.listdir(path):
            filename = path + "\\" + file
            if os.path.isdir(filename):
                self.read_dir(filename)
                return
            if file.endswith(".md"):
                try:
                    self.md_meta[filename] = self.read_meta(filename)
                except:
                    continue

    def read_meta(self, filename):
        # 读取单个文件的meta data
        meta_dict = {}
        with open(filename, "r", encoding="utf-8") as fp:
            fp.readline()   # <!--
            meta_dict["author"] = fp.readline().split(":")[1].strip()
            meta_dict["date"] = fp.readline().split(":")[1].strip()
            meta_dict["title"] = fp.readline().split(":")[1].strip()
            meta_dict["tags"] = re.split(
                "[ ,]", fp.readline().split(":")[1].strip())
            meta_dict["summary"] = fp.readline().split(":")[1].strip()
            cates = re.split("[\\\/]", filename)
            meta_dict["category"] = "未分类" if len(cates) < 3 else cates[1]
            fp.readline()   # -->
            while len(meta_dict["summary"]) < 150:
                line = fp.readline()
                if not line:
                    break
                meta_dict["summary"] = meta_dict["summary"] + fp.readline()
        return meta_dict

    def add_info(self, filename):
        # 新增单个文件meta data
        try:
            meta_data = self.read_meta(filename)
        except:
            return
        # 存入元数据数组
        self.md_meta[filename] = meta_data
        # 存入tags
        for t in meta_data["tags"]:
            if t in self.tags.keys():
                self.tags[t].append(filename)
            else:
                self.tags[t] = [filename]

    def remove_info(self, filename):
        # 移除单个文件信息
        filename.replace("\\\\", "\\")
        # 移除meta data
        if filename not in self.md_meta.keys():
            return
        tags_to_remove = self.md_meta[filename]["tags"]
        del self.md_meta[filename]
        # 移除tags
        for key in tags_to_remove:
            if key in self.tags.keys():
                self.tags[key].remove(filename)

    @deprecate
    def renew_files(self, diff_file):
        for file in diff_file:
            self.remove_info(file)
            self.add_info(file)

    def renew_file(self, file):
        self.remove_info(file)
        self.add_info(file)


if __name__ == "__main__":
    m = MDInfo()
