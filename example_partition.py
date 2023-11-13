def count_partition(n, m):
    """Count partitions
    
    >>> count_partition(6, 4)
    9
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partition(n - m, m)
        without_m = count_partition(n, m - 1)
        return with_m + without_m
    


def count_partition_simplified(n, m):
    """Count partitions
    
    >>> count_partition_simplified(6, 4)
    9
    """
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == 0:
            exact_match = 1
        with_m = count_partition(n - m, m)
        without_m = count_partition(n, m - 1)
        return with_m + without_m + exact_match
    
def list_partition(n, m):
    """List partition
    
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in list_partition(n - m, m)]
        withcout_m = list_partition(n, m - 1)
        return with_m + withcout_m + exact_match
    
print(list_partition(6, 4))