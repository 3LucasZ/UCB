class Link:
    def __init__(self, first, rest=None):
        self.first=first
        self.rest=rest
    
    def __str__(self):
        return str(self.first) + ("" if self.rest is None else ", " + str(self.rest))
    
def range_link(start, end):
    if start >= end:
        return None
    return Link(start, range_link(start + 1, end))

def map_link(f, s):
    if s == None:
        return None
    return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    if s == None:
        return None
    if f(s.first):
        return Link(s.first, filter_link(f, s.rest))
    return filter_link(f, s.rest)

def add(s, v):
    if v <= s.first:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.rest == None:
        s.rest = Link(v, None)
    else:
        add(s.rest, v)

x = range_link(1, 10) 
print(x)
print(map_link(lambda x: x*10, x))
print(filter_link(lambda x: x%2==0, x))
print(x)
add(x, 3.5)
add(x, 9.5)
print(x)