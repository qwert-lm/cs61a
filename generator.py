def plus_minus(x):
    yield x
    yield -x 

def evens(start, end):
    even = start + (start % 2)
    while even < end:
        print("before yeild statement")
        yield even
        print("after yield statement")
        even += 2

def countdown(k):
    if k >= 0:
        yield k
        yield from countdown(k - 1)
        
def prefix(s):
    if s :
        yield from prefix(s[:-1])
        yield s

t = prefix("abcde")
print(list(t))