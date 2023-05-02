from data_structures.hashtable.hashtable import  Hashtable
import string


def first_repeated_word(str):
    """
    This function takes a string as input and returns the first word that occurs more than once.
    If there is no repeated word in the string, it returns None.
    """
    # # Remove all punctuation marks from the string
    stripped = str.translate(str.maketrans('', '', string.punctuation))

    # Split the string into words and convert them to lowercase
    words = stripped.lower().split()

    # Create a dictionary to keep track of the number of occurrences of each word
    word_count = {}

    # Iterate over the words in the string
    for word in words:
        # If the word is already in the dictionary, return it
        if word in word_count:
            return word
        # Otherwise, add the word to the dictionary with a count of 1
        else:
            word_count[word] = 1

    # If no repeated word was found, return None
    return None


