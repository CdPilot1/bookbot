from stats import get_num_words
from stats import count_characters

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

from stats import count_characters

def main():
    print(get_num_words('books/frankenstein.txt'), "words found in the document.")
    print(count_characters('books/frankenstein.txt'))
main()