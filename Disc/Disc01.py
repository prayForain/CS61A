#Disc 1 Control and Environments
#pass-test


#1.1

def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return temp < 60 or raining

#1.2

def square(x):
    """
    >>> square(so_slow(5))
    # infinite loop
    """
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x += 1
    return x / 0

#1.3

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True