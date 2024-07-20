def f(s): # in iterable s | out generator | yields one by one x[::-1] where x is next in line of s
    yield from map(lambda x: x[::-1], s)

def next_next(s): # in iterator or generator | print next | out next
    print(next(s))
    return next(s)

def gen1(s): # in iterable s | out generator | yield stuff from f
    yield f(s) # f(s) is a generator object
    yield from f(s) # basically a refactor of f(s)
    print("Warmed up!")

str1 = gen1(['i','<3','cs61a','!'])
print(next(str1))
print(next(str1))
print(next_next(str1))
# print(next_next(str1))