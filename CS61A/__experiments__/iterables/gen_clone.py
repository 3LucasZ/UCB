def fork(t):
    s = []
    def copy():
        i=0
        while True:
            if i == len(s):
                s.append(next(t))
            yield s[i]
            i += 1
    return copy(), copy()

lst = [1, 2, 3, 1, 2, 3]
print(lst)
a, b = fork(iter(lst))
print([next(a), [next(b), next(b), next(b)], next(a), [next(b), next(b), next(b)], next(a)])