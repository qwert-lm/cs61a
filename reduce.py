
from operator import add, mul


def reduce(f, s, initial):
    """Combine elements of s using f starting with initial
    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    if not s:
        return initial
    para1 = s[0]
    para2 = initial
    n = len(s)
    if n == 1:
        return f(para1, para2)
    else:
        return reduce(f, s[1:], f(para1, para2))
    