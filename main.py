from stats import get_num_words
def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def main():
    print(get_num_words('books/frankenstein.txt'), "words found in the document.")

main()