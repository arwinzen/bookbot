
# need def keyword to define functions in python
def main():
    book_path = 'books/frankenstein.txt'
    text = open_book(book_path)
    num_words = get_num_words(text)
    char_count_dict = get_character_count(text)
    print_report(book_path, num_words, char_count_dict)

def open_book(book):
    with open(book) as f:
        contents = f.read()
    return contents

def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    # create an empty dictionary
    char_count = {}
    
    # loop over each word in the text
    # if word doesn't exist, initialise in dict to 1
    # else add 1 to that character count
    for i in range(len(text)):
        word = text[i].lower()

        if word.isalpha() == False:
            continue
  
        if word in char_count:
            char_count[word] += 1
        else:
            char_count[word] = 1
    return char_count

def print_report(book_path, num_words, char_count_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} found in the document\n")

    sorted_dict = dict(sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True))

    for char in sorted_dict:
        print(f"The '{char}' character was found {char_count_dict[char]} times")

    print(f"--- End report ---")


main()
