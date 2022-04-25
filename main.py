# -*- coding:utf-8 -*-

import sys
from flask import Flask, abort, request
from flask import render_template
from flask_sqlalchemy import Pagination
from gevent import pywsgi
import mdtex2html

from mdinfo import MDInfo
from new import newMD
from watch import DirMonitor

app = Flask(__name__)
app.config.from_pyfile("app.conf")


def get_meta_by_page(meta_data, page):
    if app.config["ITEMS_PER_PAGE"] * (page - 1) >= len(meta_data):
        abort(400)
    start = app.config["ITEMS_PER_PAGE"] * (page - 1)
    end = len(meta_data) if app.config["ITEMS_PER_PAGE"] * \
        page >= len(meta_data) else app.config["ITEMS_PER_PAGE"] * page
    dict_slice = {}
    for key in list(meta_data.keys())[start:end]:
        dict_slice[key] = meta_data[key]
    return dict_slice


@app.route("/")
def index():
    md_info.sort()
    page = request.args.get("page", 1, type=int)
    pagination = Pagination(md_info.md_meta, total=len(
        md_info.md_meta), page=page, per_page=app.config["ITEMS_PER_PAGE"], items=get_meta_by_page(md_info.md_meta, page))
    return render_template("index.html", **{"meta_data": get_meta_by_page(md_info.md_meta, page), "pagination": pagination, "title": app.config["TITLE"], "slogan": "slogan"})


@app.route("/blog")
def blog():
    id = request.args.get("id", type=str)
    with open(md_info.md_meta[id]["path"], "r", encoding="utf-8") as fp:
        content = fp.read()
    html = mdtex2html.convert(
        content, extensions=["codehilite", "nl2br", "toc", "fenced_code", "abbr", "fenced_code", "tables"])
    return render_template("blog.html", **{"html": html, "meta": md_info.md_meta[id], "title": md_info.md_meta[id]["title"], "slogan": md_info.md_meta[id]["title"]})


@app.route("/tag")
def tag():
    tag_list = {}
    max = 0
    for tag in md_info.tags:
        if max < len(md_info.tags[tag]):
            max = len(md_info.tags[tag])
        tag_list[tag] = len(md_info.tags[tag])
    for tag in tag_list:
        tag_list[tag] = 0.8 + tag_list[tag] * 1.5 / max
    return render_template("tag.html", **{"tags": tag_list, "title": "Tag", "slogan": "Tag"})


@app.route("/tag/<name>")
def tag_view(name):
    sort = request.args.get("sort", False, type=bool)
    page = request.args.get("page", 1, type=int)
    md_info.refresh_tag_slice(name, sort)
    pagination = Pagination(md_info.tag_meta_slice[name], total=len(
        md_info.tag_meta_slice[name]), page=page, per_page=app.config["ITEMS_PER_PAGE"], items=get_meta_by_page(md_info.tag_meta_slice[name], page))
    return render_template("tag_view.html", **{"meta_data": get_meta_by_page(md_info.tag_meta_slice[name], page), "pagination": pagination, "title": name, "slogan": name})


@app.route("/category")
def category():
    category_list = {}
    max = 0
    for cate in md_info.category:
        if max < len(md_info.category[cate]):
            max = len(md_info.category[cate])
        category_list[cate] = len(md_info.category[cate])
    for cate in category_list:
        category_list[cate] = 0.5 + category_list[cate] * 1.5 / max
    return render_template("category.html", **{"category": category_list, "title": "Category", "slogan": "Category"})


@app.route("/category/<name>")
def category_view(name):
    sort = request.args.get("sort", False, type=bool)
    page = request.args.get("page", 1, type=int)
    md_info.refresh_category_slice(name, sort)
    pagination = Pagination(md_info.category_meta_slice[name], total=len(
        md_info.category_meta_slice[name]), page=page, per_page=app.config["ITEMS_PER_PAGE"], items=get_meta_by_page(md_info.category_meta_slice[name], page))
    return render_template("category_view.html", **{"meta_data": get_meta_by_page(md_info.category_meta_slice[name], page), "pagination": pagination, "title": name, "slogan": name})


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(newMD(sys.argv[1]))
        exit(0)

    md_info = MDInfo()

    monitor = DirMonitor(r"md", md_info)
    monitor.start()

    server = pywsgi.WSGIServer((app.config["HOST"], app.config["PORT"]), app)
    server.serve_forever()
