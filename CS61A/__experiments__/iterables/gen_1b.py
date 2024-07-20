def fgen():
    yield 1

gen = fgen()
print(next(gen))
# print(next(gen))

def fgen():
    yield from [1,2,3,4,5]
gen = fgen()
print(next(gen))
print(next(gen))