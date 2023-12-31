def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    if not branches(tree):
        return True
    else:
        return False

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left) + label(right), [left, right])

def count_leaves(t):
    """count the leaves of tree t"""
    if is_leaf(t):
        return 1
    else:
        branches_sum = [count_leaves(branch) for branch in branches(t)]
        return sum(branches_sum)
    
def leaves(tree):
    """Returen a list containing the leaf labels of tree"""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(tree) for b in branches(tree)], [])
    
def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        return tree(label(t), [increment_leaves(b) for b in branches(t)])

def increment(t):
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)
    
numbers = tree(3, [tree(4), 
                   tree(5, [tree(6), tree(7)]),
                   tree(12)])

haste = tree('h', [tree('a', [tree('s'),
                              tree('t')]),
                   tree('e')])

def print_sums(t, so_far):
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)
            
def count_paths(t, total):
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - label(t)) for b in branches(t)])

def list_paths(t, value):
    """List all path to value node
    
    >>> t2 = tree(2, [tree(3), tree(4, [tree(6)]), tree(5)])
    >>> list_paths(t2, 6)
    [[2, 4, 6]]
    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> list_paths(t1, 6)
    [[1, 2, 4, 6]]
    """
    res = []
    if label(t) == value and is_leaf(t):
        return [[label(t)]]
    else:
        for branch in branches(t):
            branch_path = list_paths(branch, value)
            for path in branch_path:
                res.append([label(t)] + path)
    return res

# t1 = t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
# print(list_paths(t1, 6))
# t2 = tree(2, [tree(3), tree(4, [tree(6)]), tree(5)])
# print_tree(t2)
# print(list_paths(t2, 6))
