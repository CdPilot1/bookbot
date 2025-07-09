import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path_to_book = sys.argv[1]

from stats import get_num_words
from stats import count_characters
from stats import sorted_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

from stats import count_characters

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at", (path_to_book), "...")
    print("----------- Word Count ----------")
    print("Found", get_num_words(path_to_book), "total words")
    print("--------- Character Count -------")
    sorted_chars = sorted_char_count(path_to_book)
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['count']}")
main()