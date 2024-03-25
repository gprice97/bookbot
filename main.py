def main():
    book_path = "books/Frankenstein.txt"
    book_text = get_text(book_path)
    word_count = get_word_count(book_text)
    letter_count = get_letter_count(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(letter_count)
    print("----- Beginning of Book Report of " + book_path.split("/")[1] + " -----\n")
    print("A total of " + word_count + " words were found in the document\n")

    for list_item in chars_sorted_list:
        if not list_item["letter"].isalpha():
            continue
        print("The '" + str(list_item['letter']) + "' character was found " + str(list_item['count']) + " times.")
    print("\n----- End Report -----")

def sort_dict(dict):
    return dict["count"]

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"letter": char, "count": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_dict)
    return sorted_list

def get_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return str(len(text.split()))
    
letter_dict = {}   
# letter_dict = {
#     'a': 0,
#     'b': 0,
#     'c': 0,
#     'd': 0,
#     'e': 0,
#     'f': 0,
#     'i': 0,
#     'j': 0,
#     'k': 0,
#     'l': 0,
#     'm': 0,
#     'n': 0,
#     'o': 0,
#     'p': 0,
#     'q': 0,
#     'r': 0,
#     's': 0,
#     't': 0,
#     'u': 0,
#     'v': 0,
#     'w': 0,
#     'x': 0,
#     'y': 0,
#     'z': 0
# } 

def get_letter_count(book_text):
    for word in book_text:
        lowercase_word = word.lower()
        letters = lowercase_word.split()
        for letter in letters:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1

    return letter_dict

main()