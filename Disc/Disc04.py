#Disc 4 Recursion & Lists
#pass-test

#1.1
def count_stair_ways(n):
    """
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(5)
    8
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

#1.2
def count_k(n, k):
    """
    >>> count_k(3, 3)
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1)
    1
    """
    if n == 1:
        return 1
    elif n < k:
        return count_k(n, k-1)
    elif n == k:
        return count_k(n, k-1) + 1
    elif n > k:
        sum, i = 0, 1
        while i <= k:
            sum += count_k(n - i, k)
            i += 1  #always forget it
        return sum

#2.1
'''
>>> a = [1, 5, 4, [2, 3], 3]
>>> print(a[0], a[-1])
1 3

>>> len(a)
5

>>> 2 in a
True

>>> 4 in a
True

>>> a[3][0]
2

'''

#2.2
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(len(s)) if i % 2 == 0]

#2.3
def max_product(s):
    """Return the maximum product that can be formed using non_consecutive elements of s.

    >>> max_product([10,3,1,9,2])
    90
    >>> max_product([5,10,5,10,5])
    125
    >>> max_product([])
    1
    """
    if s == []: #it maybe can improve
        return 1
    if len(s) == 1:
        return s[0]
    elif len(s) == 2:
        return s[0] if s[0] > s[1] else s[1]
    elif len(s) >= 3:
        use_s0 = s[0] * max_product(s[2:])
        not_use_s0 = max_product(s[1:])
        return use_s0 if use_s0 > not_use_s0 else not_use_s0
