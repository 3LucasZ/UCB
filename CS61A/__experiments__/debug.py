def simple():
    return 3

def make_averaged(original_function, samples_count=1000):
    def extended_function(*args):
        n = samples_count
        ret = 0
        while n:
            ret += original_function(*args)
            n -= 1
        return ret
    return extended_function

ext = make_averaged(simple, 1000)
print(ext())