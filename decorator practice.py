import time


def timer(func):
    def wrapper(*args, **kwargs):
        result1 = time.time()
        func(args, kwargs)
        result2 = time.time()
        result = (result2) - (result1)
        print(result)
        return result
    return wrapper


@timer
def count_to_million(args, kwargs):
    for i in range(1000000):
        pass


count_to_million()
