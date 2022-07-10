def cache_func(function):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            rv = function(*args)
            cache[args] = rv
            return rv
    return wrapper


@cache_func
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    multiplier(1)
    multiplier(2)
    multiplier(3)
    multiplier(1)
