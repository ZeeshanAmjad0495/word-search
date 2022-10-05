'''Dictionary using a json file.'''
import json
from pathlib import Path


def json_to_dict(json_file: Path) -> dict | None:
    '''Reads a json file and maps it onto a dictionary and returns it.'''
    data = None
    with open(json_file) as json_file:
        data = json.load(json_file)
    return data


def search_word(dictionary: dict, word: str) -> dict | None:
    '''Find the exact match for the word in the dictionary.'''
    return {word: dictionary[word]}


def match_strings(string: str, word: str) -> bool:
    '''Match two string to see if there are three or more consecutive matching letters.'''
    index = 0
    for char in string:
        if char != word[index]:
            return False
        index += 1
    if index >= 3:
        return True


def search_matching_words(dictionary: dict, word: str) -> dict | None:
    '''Search words that match the original word.'''
    matching_words = {}
    for key, value in dictionary.items():
        if match_strings(key, word):
            matching_words[key] = value
    return matching_words


def look_in_the_dictionary() -> dict | None:
    '''Take input from the user and search it in the dictionary.'''
    file = Path(
        "dictionary.json")
    dictionary = json_to_dict(file)
    word = input('Enter the word you want to search: ').lower()
    exact_match = search_word(dictionary, word)
    if exact_match:
        return exact_match
    approximate_matches = search_matching_words(dictionary, word)
    if not approximate_matches:
        print('Word not found')
    else:
        return approximate_matches


if __name__ == '__main__':
    print(look_in_the_dictionary())
