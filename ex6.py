import re


def count_words(text: str) -> dict:
    """
    this function modify each word in the text and insert it to a dict a long side the length of the word
    @param text: the given string
    @return : dict of the  modified words ( lower cased )  and each word length
    """
    words = {word: len(word) for word in re.sub(r'\W+', ' ', text).lower().split()}
    return words
