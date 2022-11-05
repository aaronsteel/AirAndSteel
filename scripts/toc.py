import os
from datetime import date
from utils import parse_file_metadata

def generate_toc():
    header = """---
title: On Site Contents (By Article)
description: "aka the Table of Contents"
date: Sept 02 2022
---

Here's the table of contents, sorted by date. It's autogenerated with a script.

TODO: set up the ability to also run it automatically, on commit or build.
    """
    footer = """---

index tags: Site Info, Table of Contents, Organization, Site Map

---
"""
    toc_filename = "on-site-contents-by-article.mdx"

    directory = '../posts'
    print(os.listdir(directory))

    list_of_posts = []

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            f_tuple = parse_file_metadata(f, filename)
            if f_tuple:
                list_of_posts.append(f_tuple)

    list_of_posts.sort(key=lambda x: x[1])

    # remove toc if it exists
    path_to_toc = os.path.join(directory, toc_filename)
    if os.path.exists(path_to_toc):
        os.remove(path_to_toc)
    else:
        print("toc didn't exist")

    toc_file = open(path_to_toc, "w")
    toc_file.write(header)
    last_month = -1
    for post_tuple in list_of_posts:
        title, date, desc, filename = post_tuple
        post_link = f"/posts/{filename.split('.')[0]}"
        if date.month != last_month:
            toc_file.write(f"\n---\n\n## {date:%B %Y}\n")
            last_month = date.month
        toc_file.write(f"[{title}]({post_link}) - {date} - {desc}\n\n")
    toc_file.write(footer)
    toc_file.close()

if __name__ == "__main__":
    generate_toc()