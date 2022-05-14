def full_names(first_names: list, last_names: list, *min_length: any) -> list:
    """ this function accepts two lists and optional variable ,
        creates full name from the two lists , and add it if the full name is bigger if the min length """
    """
    this function creates list of full names that its length bigger than the min length from the lists
     @param first_names: the list of the first names 
     @param last_names : the list of the last names 
     @:return : list of the full names 
    """
    if not min_length:
        full_name_minimum_length = 0
    else:
        full_name_minimum_length = min_length[0]

    full_names_combined = [first_name.capitalize() + " " + last_name.capitalize()
                           for first_name in first_names for last_name in last_names
                           if len(first_name + last_name) > full_name_minimum_length]
    return full_names_combined
