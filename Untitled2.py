'''
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self
'''

'''
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
            
'''

def flatten(nested):
    if isinstance(nested, list):
        for element in nested:
            yield from flatten(element)
    else:
        yield nested

def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new

def countdown(n):
    print("Counting down from", n)
    while n >= 0:
        newvalue = (yield n)
        # if a new value got send in, reset n with it
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1

def fn_sigma(begin, end, count, step):
    return (step / 2.) * pow(count, 2) + (begin - step / 2.) * count
