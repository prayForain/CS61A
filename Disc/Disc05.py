#Disc 5 Trees, Binary Numbers
#pass-test
#But I really do not know why the solution of 2.2 works.

# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches) # The list function is really important


def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


#1.1
def height(t):
    """Return the height of a tree.
    
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        return max([height(b) + 1 for b in branches(t)])

#1.2
def max_path_sum(t):
    """Return the maximum path sum of the tree.
    
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        return max([max_path_sum(b) + label(t) for b in branches(t)])

#1.3
def square_tree(t):
    """Return a tree with the square of every element in t.
    
    >>> numbers = tree(1, [tree(2, [tree(3), tree(4)]), tree(5, [tree(6, [tree(7)]), tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    new_label = label(t)**2
    if is_leaf(t):
        return tree(new_label)
    else:
        bs = [square_tree(b) for b in branches(t)]
        return tree(new_label, bs)

#1.4
def find_path(tree, x):
    """Return a list that from the root to the node containing x, if list don't exist, return None.
    
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)
    """
    if label(tree) == x:
        return [x]
    else:
        for b in branches(tree):
            if find_path(b, x):
                return [label(tree)] + find_path(b, x)
            
#2.1
"""
    Decimal     Binary
    5           101
    10          1010
    14          1110
    37          100101
    2           10
    42          101010
    101         1100101    
"""
#2.2
def prune_binary(t, nums):
    """
    >>> t = tree('1', [tree('0', [tree('0'), tree('1')]), tree('1', [tree('0')])])
    >>> new_tree = prune_binary(t, ['01', '110', '100'])
    >>> print_tree(new_tree)
    1
      0
        0
      1
        0
    >>> t = tree('1', [t, tree('1', [tree('0')])])
    >>> new_tree = prune_binary(t, ['1101'])
    >>> print_tree(new_tree)
    1
      1
        0
          1
    """
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [num[1:] for num in nums]
        new_branches =[]
        for b in branches(t):
            pruned_branch = prune_binary(b, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
        return tree(label(t), new_branches)
