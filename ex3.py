import time


def timer(f: callable, *items: any) -> float:
    """
    this function measures how long it took for the given function to complete the task on the objects
    @param f : the given function
    @param items: the parameters passed to the function
    @return : the time measured to complete the task
    """
    start = time.time()
    f(items)
    end = time.time()
    return end - start
