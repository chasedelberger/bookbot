from sys import argv, exit
from stats import get_num_words, get_chars_dict, get_sorted_dict

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        book_path = argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        letter_dict = get_chars_dict(text)
        sorted_dict = get_sorted_dict(letter_dict)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for pair in sorted_dict:
            char = list(pair.keys())[0]
            count = list(pair.values())[0]
            if char.isalpha():
                print(f"{char}: {count}")
        print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
