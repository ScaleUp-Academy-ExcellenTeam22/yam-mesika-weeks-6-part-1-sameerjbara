def word_length(str):
    """ return the length of each word in the string"""
    words=str.split()
    return [len(word) for word in words ]