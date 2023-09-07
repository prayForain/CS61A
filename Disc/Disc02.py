#Disc 2 Higher Order Functions
#pass-test

#1.1

def keep_ints(cond, n):
    """
    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i = 1
    while i <= n:
        if cond(i):
            print(i)

#1.2

def make_keeper(n):
    """
    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def keep(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
    return keep

#1.7

def print_delayer(x):
    """
    >>> f = print_delayer(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi")
    5
    <function print_delayer>
    """
    def delay_print(y):
        print(x)
        return print_delayer(y)
    return delay_print

#1.8

def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_printsss>
    """
    def inner_print(x):
        if n == 0:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print
