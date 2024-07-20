def f(x):
    def g(y):
        def h(z):
            return x * y * z
        return h
    return g

print(f(2)(3)(4))