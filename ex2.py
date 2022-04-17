def get_positive_numbers():
    """ gets from the user list of numbers (as str) conver it to int and insert it to a list,
    run on the list and keeps only positive numbers"""
    numbers=[int(x) for x in input("enter a list of numbers : ").split(",")]
    positive_numbers=[number for number in numbers if number>0]
    return positive_numbers