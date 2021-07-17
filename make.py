#!/usr/bin/python3

import os

def main():
    glbs = os.listdir("glbs")

    with open("templates/page.html", "r") as f:
        page_template = f.read()

    for filename in glbs:
        context = {"filename": filename}
        content = page_template.format(**context)
        with open(f"pages/{filename}.html", "w") as page:
            page.write(content)

    with open("templates/index.html") as f:
        index_template = f.read()

    item = '<li><a href="pages/{filename}.html" target="_blank">{filename}</a></td></li>'
    page_list = '\n    '.join(item.format(filename=filename) for filename in glbs)
    context = {"page_list": page_list}
    content = index_template.format(**context)
    with open("index.html", "w") as index:
        index.write(content)


if __name__ == "__main__":
    main()
