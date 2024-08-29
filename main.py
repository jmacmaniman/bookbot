def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lowered_text = text.lower()
    num_words = get_num_words(lowered_text)
    num_chars = get_num_chars(lowered_text)
    list_of_dicts = convert_dict_to_list(num_chars)
    list_of_dicts.sort(reverse=True, key=sort_on)
    print_report(num_words, list_of_dicts)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    char_counter = {}
    for char in text:
        if char.isalpha():
            if char not in char_counter:
                char_counter[char] = 1
            else:
                char_counter[char] += 1
    return char_counter

def convert_dict_to_list(dict_char_count):
    new_list = []
    for key in dict_char_count:
        new_dict = {"char": key, "num": dict_char_count[key]}
        new_list.append(new_dict)
    return new_list

def sort_on(d):
    return d["num"]

def print_report(word_count, sorted_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for entry in sorted_list:
        print(f"The '{entry['char']}' character was found {entry['num']} times")
    print("--- End report ---")

main()