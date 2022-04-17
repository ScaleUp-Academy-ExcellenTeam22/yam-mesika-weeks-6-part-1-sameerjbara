def my_filter(function,iterable):
    """ run on the iterable and execute the function , we add the element only if the retrun value of 
    the function is not false or 0"""
    filtered=[]
    for element in iterable:
        result=function(element)
        if result!="false" and result!=0 :
            filtered.append(element)
    return filtered


