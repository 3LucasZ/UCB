def pack(n):
    """Yield the ways to park an equal number of cars and motorcycles
    in n adjacent spots with no motorcycle adjacent to a car and no
    empty spot adjacent to another empty spot.
    
    >>> sorted(pack(4))
    ['%.<>', '<>.%']
    >>> sorted(pack(7))
    ['%%.<><>', '<><>.%%']
    >>> sorted(pack(8))
    ['%%.<>.<>', '%%.<><>.', '%.%.<><>', '%.<><>.%', '.%%.<><>',
    '.<><>.%%', '<>.%%.<>', '<>.<>.%%', '<><>.%%.', '<><>.%.%']
    """

    def f(n, k):
        if n == 0 and k == 0:
            yield ''
        elif n > 0:
            yield from g(n-1, k-1, '<', '%' )
            yield from g(n-1, k,   '.', '.' )
            yield from g(n-2, k+1, '%', '<>')
    def g(n, k, no, yes):
        pass
    yield from f(n, 0)

print(sorted(pack(7)))