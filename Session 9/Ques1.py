class Counting:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self): 
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration
counting = Counting(15)
for x in counting:
    print(x)