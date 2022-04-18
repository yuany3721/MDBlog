# -*- coding:utf-8 -*-

import os
import re


class MDInfo:
    md_meta = {}    # 存放md文档元数据
    tags = {}       # 存放文档tags
    tag_meta_slice = {}  # tag对应的文档元数据切片
    category = {}   # 存放文档category
    category_meta_slice = {}    # category对应的文档元数据切片
    sort_flag = False   # 是否排序

    def __init__(self):
        self.__read_dir("md")
        for filename in self.md_meta.keys():
            for t in self.md_meta[filename]["tags"]:
                if t in self.tags.keys():
                    self.tags[t].append(filename)
                else:
                    self.tags[t] = [filename]
            if self.md_meta[filename]["category"] in self.category.keys():
                self.category[self.md_meta[filename]
                              ["category"]].append(filename)
            else:
                self.category[self.md_meta[filename]["category"]] = [filename]

    def __read_dir(self, path):
        # 读取path下所有md文件并放入元数据数组中
        for file in os.listdir(path):
            filename = path + "\\" + file
            if os.path.isdir(filename):
                self.__read_dir(filename)
            if file.endswith(".md"):
                try:
                    self.md_meta[filename] = self.__read_meta(filename)
                except:
                    continue

    def __read_meta(self, filename):
        # 读取单个文件的meta data
        meta_dict = {}
        with open(filename, "r", encoding="utf-8") as fp:
            fp.readline()   # <!--
            meta_dict["author"] = fp.readline().split(":")[1].strip()
            meta_dict["date"] = fp.readline().split(":")[1].strip()
            meta_dict["title"] = fp.readline().split(":")[1].strip()
            meta_dict["tags"] = re.split(
                "[ ,]", fp.readline().split(":")[1].strip().replace("  ", " "))
            meta_dict["summary"] = fp.readline().split(":")[1].strip()
            cates = re.split("[\\\/]", filename)
            meta_dict["category"] = "未分类" if len(cates) < 3 else cates[1]
            meta_dict["datenum"] = self.__date_to_datenum(meta_dict["date"])
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
            meta_data = self.__read_meta(filename)
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
            # 标记slice变动，更新对应tag下slice信息
            if t in self.tag_meta_slice:
                self.tag_meta_slice[t][filename] = self.md_meta[filename]
        # 存入category
        if meta_data["category"] in self.category.keys():
            self.category[meta_data["category"]].append(filename)
        else:
            self.category[meta_data["category"]] = [filename]
        # 标记slice变动，更新对应catogery下slice信息
        if meta_data["category"] in self.category_meta_slice:
            self.category_meta_slice[meta_data["category"]
                                     ][filename] = self.md_meta[filename]
        self.sort_flag = False      # 插入后序列可能变为无序

    def remove_info(self, filename):
        # 移除单个文件信息
        filename.replace("\\\\", "\\")
        # 移除meta data
        if filename not in self.md_meta.keys():
            return
        tags_to_remove = self.md_meta[filename]["tags"]
        category_to_remove = self.md_meta[filename]["category"]
        del self.md_meta[filename]
        # 移除tags
        for key in tags_to_remove:
            if key in self.tags.keys():
                self.tags[key].remove(filename)
                if len(self.tags[key]) == 0:
                    del self.tags[key]
        # 移除tag_meta_slice
        for slice in self.tag_meta_slice:
            if len(slice) > 0 and filename in slice.keys():
                del slice[filename]
        # 移除category
        if category_to_remove in self.category.keys():
            self.category[category_to_remove].remove(filename)
        # 移除category_meta_slice
        for slice in self.category_meta_slice:
            if filename in slice.keys():
                del slice[filename]

    def renew_file(self, file):
        self.remove_info(file)
        self.add_info(file)

    def __date_to_datenum(self, date):
        splits = date.split("-")
        datenum = 0
        for s in splits:
            datenum = datenum * 100 + int(s)
        return datenum

    def sort(self):
        if not self.sort_flag:
            self.md_meta = dict(sorted(self.md_meta.items(),
                                       key=lambda x: -x[1]["datenum"]))
            self.sort_flag = True

    def refresh_tag_slice(self, tag_name, sort):
        # 获取最新tag slice
        if tag_name not in self.tag_meta_slice.keys():
            for filename in self.tags[tag_name]:
                if tag_name not in self.tag_meta_slice.keys():
                    self.tag_meta_slice[tag_name] = {}
                self.tag_meta_slice[tag_name][filename] = self.md_meta[filename]
            pass
        if sort:
            self.tag_meta_slice[tag_name] = dict(
                sorted(self.tag_meta_slice[tag_name].items(), key=lambda x: -x[1]["datenum"]))

    def refresh_category_slice(self, category_name, sort):
        # 获取最新category slice
        if category_name not in self.category_meta_slice.keys():
            for filename in self.category[category_name]:
                if category_name not in self.category_meta_slice.keys():
                    self.category_meta_slice[category_name] = {}
                self.category_meta_slice[category_name][filename] = self.md_meta[filename]
            pass
        if sort:
            self.category_meta_slice[category_name] = dict(sorted(
                self.category_meta_slice[category_name].items(), key=lambda x: -x[1]["datenum"]))


if __name__ == "__main__":
    m = MDInfo()
