def get_letters() -> list:
    """
    this function create a list of all the letters between a-z and A-Z
    @param : none
    @return: list of all the letters
    """
    return [chr(letter) for letter in range(ord('a'), ord('z'))] \
           + [chr(letter) for letter in range(ord('A'), ord('Z'))]


print(get_letters())
