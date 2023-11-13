def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.
       At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    
    def helper(x):
        if x == 1:
            yield x
        elif x % 2 == 0:
            yield x // 2
        else:
            yield x * 3 + 1
    yield n
    yield from hailstone(helper(n))
            
            