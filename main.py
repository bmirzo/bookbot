import sys
from stats import get_num_words, char_count, sorted_list_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1] 

    book = get_book_text(book_path)
    num_words = get_num_words(book)
    num_chars = char_count(book)
    sorted_num_chars = sorted_list_char_count(num_chars)
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(sorted_num_chars)):
        print(f"{sorted_num_chars[i]["char"]}: {sorted_num_chars[i]["num"]}")
    print("============= END ===============")
main()