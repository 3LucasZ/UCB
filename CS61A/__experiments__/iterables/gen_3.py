def fgen(s):
    return map(lambda x:x[::-1], s)

print(fgen(['i','love','Jesus']))

def fgen(s):
    yield map(lambda x:x[::-1], s)

print(fgen(['i','love','Jesus']))

def fgen(s):
    yield from map(lambda x:x[::-1], s)

x = fgen(['i','love','Jesus'])
print(next(x),next(x),next(x))