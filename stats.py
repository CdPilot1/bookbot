def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()
def get_num_words(path_to_file):
    word_count = get_book_text('books/frankenstein.txt').split()
    return len(word_count)

def count_characters(path_to_file):
    char_counts = {}
    for char in get_book_text(path_to_file).lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
