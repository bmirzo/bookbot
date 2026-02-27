def get_num_words(text):
    return len(text.split())

def char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def sorted_list_char_count(char_count):
    list_chdict = []

    for ch, num in char_count.items():
        list_chdict.append({"char": ch, "num": num})
    
    list_chdict.sort(reverse=True, key=sort_on)
    return list_chdict