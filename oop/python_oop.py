import json
import difflib


def load_dictionary(file_path):
    try:
        # Open and read the JSON file
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None


def get_definition(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        suggested_word = suggest_word(word, dictionary)
        if suggested_word:
            return f"Did you mean '{suggested_word}'? Its definition is: {dictionary[suggested_word]}"
        else:
            return "No definition found, and no similar word suggestions available."


def suggest_word(word, dictionary):
    suggestions = difflib.get_close_matches(word, dictionary.keys())
    return suggestions[0] if suggestions else None


# Main program
if __name__ == "__main__":
    dictionary = load_dictionary("dictionary.json")
    if dictionary is not None:
        word = input("Enter a word to find its definition: ")
        definition = get_definition(word, dictionary)
        print(definition)
