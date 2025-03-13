def get_num_words(book_text):
    message_list = book_text.split()
    return len(message_list)

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