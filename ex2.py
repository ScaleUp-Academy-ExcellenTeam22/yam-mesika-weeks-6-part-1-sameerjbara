def get_positive_numbers():
    """
    the function create a list of positive numbers only from the user input
    @return positive_numbers : list of the positive numbers
    """
    numbers = input("enter a list of numbers : ").split(",")
    positive_numbers = [int(x) for x in numbers if int(x) > 0]
    return positive_numbers
