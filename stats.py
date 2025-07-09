def get_num_words(path_to_file):
    word_count = get_book_text('books/frankenstein.txt').split()
    return len(word_count)