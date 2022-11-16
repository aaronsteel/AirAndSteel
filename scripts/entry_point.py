from toc import generate_toc
from index import generate_index
from categories import generate_categories
from pdf import generate_pdf

if __name__ == "__main__":
    generate_toc()
    generate_index()
    generate_categories()
    generate_pdf()