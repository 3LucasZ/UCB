def fgen():
    while True:
        yield from [1,2,3]

gen = fgen()
print(gen)
print(next(gen),next(gen),next(gen),next(gen),next(gen))
