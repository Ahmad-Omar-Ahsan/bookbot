def get_num_words(file_content:str =None):
    list_of_strings = file_content.split()
    return len(list_of_strings)

def count_characters(file_content:str = None):
    alphabet_dict = {}
    list_of_strings = file_content.split()
    for word in list_of_strings:
        for character in word:
            character = character.lower()
            alphabet_dict[character] = alphabet_dict.get(character, 0) + 1
    return alphabet_dict

def sort_on(items):
    return items['num']

def sort_dict(char_dict:dict = None):
    new_char_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            temp_dict = {"char": key, "num": value}
            new_char_list.append(temp_dict)
        else:
            continue 
    new_char_list.sort(reverse=True, key=sort_on)
    return new_char_list