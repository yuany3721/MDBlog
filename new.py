# -*- coding:utf-8 -*-

import datetime
from sre_constants import CATEGORY
from hamcrest import ends_with
from isort import file
import nanoid
import os


def newMD(filename):

    INFO_DICT = {
        "author": "yuany3721",
        "date": str(datetime.date.today()),
        "title": "",
        "tags": "",
        "summary": ""
    }

    if filename == "rand":
        filename = nanoid.generate('1234567890abcdef', 6)

    file = "md/" + filename + ".md"
    while os.path.exists(file):
        file = "md/" + nanoid.generate('1234567890abcdef', 6) + ".md"

    with open(file, "w") as fp:
        fp.write("<!--\n")
        for info in INFO_DICT:
            fp.write(info + ": " + INFO_DICT[info] + "\n")
        fp.write("-->\n")

    return file


if __name__ == "__main__":
    print(newMD(""))
