import re

def count_words(text):
    """this function gets a text, lower case and removes non-letter characters  for each word in the text,
    create a dict that contains each word and the length of the word, 
    return the dict"""
    words = {word: len(word) for word in re.sub(r'\W+',' ',text).lower().split()}
    return words

