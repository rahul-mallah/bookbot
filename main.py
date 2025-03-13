import sys
from stats import get_num_words
from stats import count_text
from stats import convert_to_sorted_dict_list

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_contents = get_book_text(sys.argv[1])
        num = get_num_words(file_contents)
        count_characters = count_text(file_contents)
        # print(count_characters)
        char_count_list = convert_to_sorted_dict_list(count_characters)
        print_report("books/frankenstein.txt", num, char_count_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(path, count, char_count_list):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {count} total words")
    print(f"--------- Character Count -------")

    for character in char_count_list:
        print(f"{character["alphabet"]}: {character["num"]}")

    print("============= END ===============")


main()