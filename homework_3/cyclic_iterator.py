from itertools import cycle


class CyclicIterator:
    def __init__(self, iterable):
        self.data = cycle(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data)


class Range2:
    def __init__(self, limit: int):
        self.temp = -1
        self.limit = limit - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.temp < self.limit:
            self.temp += 1
            return self.temp
        raise StopIteration


if __name__ == '__main__':

    # loop = CyclicIterator(Range2(4))
    # loop = CyclicIterator([1, 2, 3, 4, 5])
    # loop = CyclicIterator((1, 2, 3, 4, 5))
    # loop = CyclicIterator({1, 2, 3, 4, 5})
    loop = CyclicIterator('Ivan')

    for i in loop:
        print(i)
