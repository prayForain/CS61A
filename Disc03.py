#Disc 3 Recursion
#pass_test

#1.1
def multiply(m, n):
    """Return the product of m times n.

    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m  
    return multiply(m, n-1) + m

#1.3
def hailstone(n):
    """Print out the hailstone sequence starting at n,
    and return the number of elements in the sequence.

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
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n // 2) + 1
    else:
        return hailstone(3 * n + 1) + 1
    
#1.4
def merge(n1, n2):
    """Merges two numbers.

    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge(21, 31)
    3211
    """
    if n1 == 0 or n2 == 0:
        return n1 + n2
    if n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10
    
#1.5
def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2)
    3
    >>> incr_1(5)
    6
    """
    def repeat(times):
        if times == 0:
            return x
        else:
            return f(repeat(times - 1))
    return repeat

#1.6
def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    if prime_helper(n, 2) == n:
        return True
    else:
        return False

def prime_helper(n, k):
    if n < k:
        return 0
    elif n % k == 0:
        return k
    else:
        k += 1
    return prime_helper(n, k)   #return the minimum factor of n starting from k or 0 if not present