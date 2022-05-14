from typing import Callable


def my_filter(function: Callable[[iter], str or int], iterable: iter) -> list:
    """
    returns a list from those elements of iterable for which function returns true or 1
    @param: function: The filtering function
    @param: iterable: iterable object
    @return: the filtered list.
    """
    filtered = [element for element in iterable if function(element) not in [0, "false"]]
    return filtered


