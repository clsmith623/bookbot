def get_word_count(text):
    split_text = text.split()
    word_count = len(split_text)
    return word_count


def get_char_count(text):
    full_char_count = {}
    text = text.lower()
    char_set = set()
    for char in text:
        char_set.add(char)
    for char in char_set:
        char_count = 0
        for t in text:
            if t == char:
                char_count += 1
        full_char_count.update({char: char_count})
    return full_char_count


def sort_on(dict):
    return dict["count"]


def sort_dict(dict_to_sort):
    sorted_list = []
    for key in dict_to_sort:
        if key.isalpha():
            char_dict = {"char": key, "count": dict_to_sort[key]}
            sorted_list.append(char_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
