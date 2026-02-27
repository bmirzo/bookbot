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

def sort_on(items):
    return items["num"]

def sorted_list_char_count(char_count):
    list_chdict = []

    for ch, num in char_count.items():
        list_chdict.append({"char": ch, "num": num})
    
    list_chdict.sort(reverse=True, key=sort_on)
    return list_chdict