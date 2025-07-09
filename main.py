def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def get_word_count(path_to_file):
    word_count = get_book_text('books/frankenstein.txt').split()
    return len(word_count)

def main():
    print(get_word_count('books/frankenstein.txt'), "words found in the document.")

main()