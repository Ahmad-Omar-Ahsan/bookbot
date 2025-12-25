from stats import get_num_words, count_characters, sort_dict
import sys


def get_book_text(filepath : str = None):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(num_words: int = None, sorted_character_list: list = None, rel_path: str = None):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {rel_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for word_key in sorted_character_list:
        print(f"{word_key['char']}: {word_key['num']}")


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    rel_path = sys.argv[1]
    contents = get_book_text(filepath = rel_path)
    num_words = get_num_words(file_content = contents)
    character_dict = count_characters(file_content = contents)
    sorted_list_dict = sort_dict(char_dict = character_dict)
    print_report(num_words = num_words, sorted_character_list = sorted_list_dict, rel_path = rel_path)
    


main()