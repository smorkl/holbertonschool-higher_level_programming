
class CountedIterator():
    def __init__(self, iterable) -> None:
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        return self.count
    
    def __next__(self):
        self.count += 1
        return next(self.iterator)