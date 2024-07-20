def ggen():
    while True:
        yield from [1,2,3]

def fgen():
    yield ggen()
    yield from ggen()

def fgen():
    yield ggen()
    for i in ggen():
        yield i

gen = fgen()
print(gen)
print(next(gen),next(gen),next(gen),next(gen),next(gen))
