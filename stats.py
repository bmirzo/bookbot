def get_num_words(book):
    return len(book.split())

def char_count(book):
    char_dict = {}
    char_list = []

    words = book.split()
    for word in words:
        for char in word:
            char_list.append(char.lower())

    unique_chars = set("".join(char_list))
    for ch in unique_chars:
        char_dict[ch] = char_list.count(ch)

    return char_dict