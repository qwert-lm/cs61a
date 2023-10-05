def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return m
    else:
        return multiply(m, n - 1) + m
        
# print(multiply(100, 3))

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)
    
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i == n:
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)
# print(is_prime(15))
# print(is_prime(13))

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    def print_process(m, count):
        print(m)
        if m == 1:
            return count + 1
        elif m % 2 == 0:
            return print_process(int(m / 2), count + 1)
        else:
            return print_process(m * 3 + 1, count + 1)
    
    return print_process(n, 0)
    
# a = hailstone(10)
# print(f"return val: {a}")
# b = hailstone(1)
# print(f"return val: {b}")

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10
print(merge(21, 31))
print(merge(21, 0))
print(merge(6521, 31))