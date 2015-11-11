#import argparse

"""
parser = argparse.ArgumentParser(description="Enter the letters in your hand")
parser.add_argument('letters', type=str)
parser.parse_args()
"""

def construct_word_list():
    f = open('legal_words.txt', 'r')
    legal_words_list = []
    for line in f:
        line = line.replace("\n", '')
        legal_words_list.append(line)
    return legal_words_list


def get_rack():
    return input("What letters do you have?")


def build_frequency_dictionary(string):
    frequency_dict = dict()
    for letter in string:
        if letter in frequency_dict:
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1
    return frequency_dict

def is_constructable(word, dict):
    for letter in word:
        if ((letter in dict) and (dict[letter] > 0)):
            dict[letter] -= 1
        else:
            return False
    return True

def main():

    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

    words_list = construct_word_list()
    letters = get_rack()

    frequency_dictionary = build_frequency_dictionary(letters)
    constructable_words = []

    for word in words_list:
        if is_constructable(word, frequency_dictionary):
            constructable_words.append(word)
            frequency_dictionary = build_frequency_dictionary(letters)
        else:
            frequency_dictionary = build_frequency_dictionary(letters)

    for word in constructable_words:
        print(word)

if __name__ == '__main__':
    main()
