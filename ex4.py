def word_length(string: str) -> list:
    """ 
    this function calculate the length of each word in the string
    @param string : the given string 
    @return : list of the length of each word
    """
    words = string.split()
    return [len(word) for word in words]
