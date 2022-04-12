# -*- coding:utf-8 -*-

import sys
from flask import Flask
from flask import render_template
from gevent import pywsgi
from mdinfo import MDInfo
from new import newMD
from watch import DirMonitor

app = Flask(__name__)
app.config.from_pyfile('app.conf')
# print(app.config)
# for key in app.config:
#     print(key, app.config[key])


@app.route('/')
def index():
    return render_template("index.html", **{"meta_data": md_info.md_meta.values()})


@app.route('/blog/<title>')
def blog():
    return render_template("blog.html")


@app.route('/tag/<name>')
def tag():
    return render_template("tag.html")


@app.route('/category/<name>')
def category():
    return render_template("category.html")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(newMD(sys.argv[1]))
        exit(0)

    md_info = MDInfo()

    monitor = DirMonitor(r"md", md_info)
    monitor.start()

    server = pywsgi.WSGIServer((app.config['HOST'], app.config['PORT']), app)
    server.serve_forever()
