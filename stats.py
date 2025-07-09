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

def sorted_char_count(path_to_file):
    def sort_on(dict_item):
        return dict_item['count']
    char_count_dict = count_characters(path_to_file)
    list_of_dicts = [{'char': char, 'count': count} for char, count in char_count_dict.items() if char.isalpha()] 
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts