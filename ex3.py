import time

def timer(f,*items):
    """this function measures how long it took for the given function to complete a the task on the objects"""
    start = time.time()
    f(items)
    end = time.time()
    return (end - start)