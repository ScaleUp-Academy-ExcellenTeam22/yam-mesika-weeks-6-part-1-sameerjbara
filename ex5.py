def get_letters():
    """this function returns a list of all the letters between a-z and A-Z"""
    return [chr(letter) for letter in range(ord('a'),ord('z'))]\
      +[chr(letter) for letter in range(ord('A'),ord('Z'))]

get_letters()