def countdown(n):
    if n > 1:
        yield n
        for x in countdown(n-1):
            yield x
    
def countdown_new(n):
    if n > 1:
        yield n
        yield from countdown_new(n - 1)
        
def prefix(s):
    if s:
        yield from prefix(s[:-1])
        yield s
    
def count_partition(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partition(n-m, m)
        without_m = count_partition(n, m - 1)
        return with_m + without_m
    
def count_partition_1(n, m):
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0 
        if n == m:
            exact_match = 1
        with_m = count_partition_1(n-m, m)
        without_m = count_partition_1(n, m-1)
        return exact_match + with_m + without_m
    
def list_partition(n, m):
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [part + [m] for part in list_partition(n-m, m)]
        without_m = list_partition(n, m-1)
        return exact_match + with_m + without_m
for p in list_partition(6, 4):
    print(p)