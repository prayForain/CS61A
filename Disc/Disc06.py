#Disc 6 Nonlocal, Mutability, Iterators, Generators
#pass-test
#1. 2.2
#For the qusetion 2.4, there is something wrong in the pdf, the s after executing the command add_this_many(1, 5, s) should be [1, 2, 4, 2, 1, 5]
#instead of [1, 2, 4, 2, 1, 5 , 5]

#1.1
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n
        return g(n)
    return f


#2.1
"""
>>> s1 = [1, 2, 3]
>>> s2 = s1
[1, 2, 3]

>>> s1 is s2
True

>>> s2.extend([5, 6])
[1, 2, 3, 5, 6]

>>> s1[4]
6

>>> s1.append([-1, 0, 1])
[1, 2, 3, 5, 6, [-1, 0, 1]]

>>> s2[5]
[-1, 0, 1]

>>> s3 = s2[:]
>>> s3.insert(3, s2.pop(3))
[1, 2, 3, 5, 6, [-1, 0, 1]]

>>> len(s1)
5

>>> s1[4] is s3[6]
True

>>> s3[s2[4][1]]
1

>>> s1[:3] is s2[:3]
True

>>> s1[:3] == s2[:3]
True

"""

#2.2
def mystery(p, q):
    """
    >>> p = [2, 3]
    >>> q = [4, [p]]
    >>> mystery(q, p)
    >>> p
    [2, 3, [[[...], 2, 3]]]
    >>> q
    [4, [[2, 3, [[...]]], 2, 3]]
    """
    p[1].extend(q)
    q.append(p[1:])



#2.3
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for e in s:
        key = fn(e)
        if key not in grouped.keys():
            grouped[fn(e)] = [e]
        else:
            grouped[key] = grouped[key] + [e]
    return grouped


#2.4
def add_this_many(x, el, s):
    """
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 2, 2]
    """
    i = 0
    while i < x:
        s.append(el)
        i += 1


#3.1
"""
>>> s = [[1, 2]]
>>> i = iter(s)
>>> j = iter(next(i))
>>> next(j)
1

>>> s.append(3)
>>> next(i)
3

>>> next(j)
2

>>> next(i)
StopIteration

"""

#4.1
def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even))
    [0, 2, 4]
    >>> all_odd = (2 * y for y in range(5))
    >>> list(filter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for x in iterable:
        if fn(x):
            yield x

#4.2
def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3)
    >>> b = sequence(3, 2)
    >>> result = merge(a, b)
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    next_a = next(a)
    next_b = next(b)
    while a and b:
        if next_a < next_b:
            yield next_a
            next_a = next(a)
        elif next_a > next_b:
            yield next_b
            next_b = next(b)
        else:
            yield next_a
            next_a = next(a)
            next_b = next(b)
