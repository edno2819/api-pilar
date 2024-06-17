import unicodedata


VOWELS = "aeiou"


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([char for char in nfkd_form if not unicodedata.combining(char)])


def count_vowels(word):
    return sum(1 for char in word if remove_accents(char).lower() in VOWELS)