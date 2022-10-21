import os
import json
from utils import parse_file_metadata, copy_pdfified

posts_directory = '../posts'
pdfified_directory = './pdfified_posts'

def generate_pdfified_mdxes():
    for filename in os.listdir(posts_directory):
        old_path = os.path.join(posts_directory, filename)
        new_path = os.path.join(pdfified_directory, filename)
        if os.path.isfile(old_path):
            copy_pdfified(old_path, new_path)

def get_pdf_info():
    list_of_posts = []
    for filename in os.listdir(pdfified_directory):
        old_path = os.path.join(posts_directory, filename)
        new_path = os.path.join(pdfified_directory, filename)
        if os.path.isfile(old_path):
            f_tuple = parse_file_metadata(old_path, filename)
            if f_tuple:
                list_of_posts.append(f_tuple)

    list_of_posts.sort(key=lambda x: x[1])

    md_docs = []
    for post in list_of_posts:
        md_docs.append(os.path.join(pdfified_directory, post[3]))
    return {"mdDocs": md_docs}

def generate_and_write_pdf_info():
    generate_pdfified_mdxes()
    json_object = json.dumps(get_pdf_info(), indent=4)
    path_to_pdf_info = "./pdf_info.json"
    with open(path_to_pdf_info, "w") as pdf_info_file:
        pdf_info_file.write(json_object)

def generate_pdf():
    generate_and_write_pdf_info()
    # os.system("npm install")
    os.system("node pdf.mjs")

if __name__ == "__main__":
    generate_pdf()