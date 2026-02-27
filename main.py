from stats import get_num_words, char_count, sorted_list_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book)
    num_chars = char_count(book)
    sorted_num_chars = sorted_list_char_count(num_chars)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(sorted_num_chars)):
        print(f"{sorted_num_chars[i]["char"]}: {sorted_num_chars[i]["num"]}")
    print("============= END ===============")
main()