def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num = count_words(file_contents)
    count_characters = count_text(file_contents)
    char_count_list = convert_to_sorted_dict_list(count_characters)
    print_report("books/frankenstein.txt", num, char_count_list)


def count_words(book_text):
    message_list = book_text.split()
    return len(message_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_text(book_text):
    alphabets = {}

    lower_text = book_text.lower()
    for char in lower_text:
        if char in alphabets:
            alphabets[char] += 1
        else:
            alphabets[char] = 1
    
    return alphabets;

def sort_on(dict):
    return dict["num"]

def convert_to_sorted_dict_list(count_characters):
    char_count_list = []
    for character in count_characters:
        if character.isalpha():
            char_count_list.append({"alphabet":character, "num":count_characters[character]})

    char_count_list.sort(reverse=True, key=sort_on)

    return char_count_list

def print_report(path, count, char_count_list):
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document. \n")

    for character in char_count_list:
        print(f"The '{character["alphabet"]}' character was found {character["num"]} times")

    print("--- End report ---")


main()