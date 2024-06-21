def main():
    bookpath = "books/frankenstein.txt"
    text = get_book_text(bookpath) 
    word_count = get_word_count(text)
    character_count = get_num_characters(text) 
    list_of_dicts = dict_to_list_of_dicts(character_count)
    list_of_dicts.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {bookpath} ---")
    print(f"{word_count} words found in the document")
    for d in list_of_dicts:
        print(f"The '{d["char"]}' character was found {d["num"]} times")
    print("--- End report ---")

def sort_on(dictionary):
    return dictionary["num"]


def dict_to_list_of_dicts(dictionary):
    new_list = []
    for line in dictionary:
        if line.isalpha():
            new_list.append({"char": line, "num":dictionary[line]})
    return new_list

def get_num_characters(text):
    character_dict = {}
    text_lower_case = text.lower()
    for character in text_lower_case:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def get_word_count(text):
    words = text.split()
    return len(words)

main()