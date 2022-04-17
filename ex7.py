def full_names(first_names, last_names, *min_length):
    """ this function accepts two lists and optional variable ,
        creates full name from the two lists , and add it if the full name is bigger if the min length """
    if not min_length:
        min = 0
    else:
        min = min_length[0]

    full_names_comp = [first_name.capitalize() + " " + last_name.capitalize()
                       for first_name in first_names for last_name in last_names
                       if len(first_name + last_name) > min]
    return (full_names_comp)
