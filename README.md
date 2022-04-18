# MDBlog

基于 Flask 和 markdown 文档的轻量级博客

## 功能

- 博文列表
- 标签
- 分类
- 详情

## 配置

参见`app.conf`

## 启动

```bash
python main.py
```
服务启动后会自动监测`/md`中md文档的变化，您可以使用git等代码同步工具对此文件夹进行同步。

## 新建一个 markdown 文档

为了呈现 markdown 文档的 metadata，您可以向 `main.py` 中传入想要编写的 markdown 文档文件名以生成空的 markdown 文档：

```bash
python main.py Your-new-md-filename
```

此命令用于生成一个存放在 `md` 目录下的，拥有自定义信息模板的 markdown 文档，这些信息您可以在 `new.py` 文件中更改 `INFO_DICT` 以进行修改，例如：

```markdown
<!--
author: yuany3721
date: 2022-04-11
title:
tags:
summary:
-->
```

命令返回值为文件路径，如 `md/Your-new-md-filename.md` 。

如果文件名已存在，或者使用 `rand` 作为文件名，将会使用 `1234567890abcdef` 作为字典生成一个 6 位长度的 `nanoid` 。

## 鸣谢

[flask](https://github.com/pallets/flask)

[jinja](https://github.com/pallets/jinja)

[watchdog](https://github.com/gorakhargosh/watchdog)

[py-nanoid](https://github.com/puyuan/py-nanoid)

[mdtex2html](https://github.com/polarwinkel/mdtex2html)


