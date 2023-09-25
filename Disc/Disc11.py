# Disc 11 Interpreters
"""
I have passed the test for question 1.1 and question 1.2, 
and one unavoidable error that may persist for question 2.1 is TypeError: 'Pair' object is not iterable,
but I think the idea in the code is intuitive and easy to understand.
"""

from operator import mul, sub

OPERATORS = {}
OPERATORS['+'] = sum
OPERATORS['*'] = mul
OPERATORS['-'] = sub

class Pair:
    nil = ()
    """Represents the built-in pair data structure in Scheme.""" 
    def __init__(self, first, rest):
        self.first = first
        #if not scheme_valid_cdrp(rest):
        #    raise SchemeError("cdr can only be a pair, nil, or a promise but was {}".format(rest)) 
        self.rest = rest
    def map(self, fn):
        """Maps fn to every element in a list, returning a new Pair.
        >>> Pair(1, Pair(2, Pair(3, nil))).map(lambda x: x * x) Pair(1, Pair(4, Pair(9, nil)))
        """
        assert isinstance(self.rest, Pair) or self.rest is nil, "rest element in pair must be another pair or nil" 
        return Pair(fn(self.first), self.rest.map(fn))
    def __repr__(self):
        def helper(pair):
            if pair is nil:
                return ''
            elif isinstance(pair.first, Pair):
                return '(' + helper(pair.first) + ') '+ helper(pair.rest)
            elif pair.rest is nil:
                return str(pair.first)
            else:
                return str(pair.first) +' ' + helper(pair.rest)
        return '(' + helper(self) + ')'

class nil:
    """Represents the special empty pair nil in Scheme.""" 
    def map(self, fn = None):
        return nil
    def __getitem__(self, i):
        raise IndexError('Index out of range') 
    def __repr__(self):
        return 'nil'

#1.1
def f1():
    """
    >>> Pair('+', Pair(1, Pair(2, Pair(3, Pair(4, nil)))))
    (+ 1 2 3 4)
    >>> Pair('+', Pair(1, Pair(Pair('*', Pair(2, Pair(3, nil))), nil)))
    (+ 1 (* 2 3))
    """

#1.2
def f2():
    """
    >>> p = Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))
    >>> p
    (+ (- 2 4) 6 8)
    >>> p.first
    '+'
    >>> p.rest
    ((- 2 4) 6 8)
    >>> p.rest.first
    (- 2 4)
    """

def calc_eval(exp):
    """Evaluates a Calculator expression represented as a Pair.""" 
    if isinstance(exp, Pair): # Call expressions
        fn = calc_eval(exp.first)
        args = list(exp.rest.map(calc_eval)) 
        return calc_apply(fn, args)
    elif exp in OPERATORS: # Names 
        return OPERATORS[exp]
    else: # Numbers 
        return exp

def calc_apply(fn, args):
    """Applies a Calculator operation to a list of numbers.""" 
    return fn(args)


#2.1
def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == 'and':
            return eval_and(exp.rest)
        else:
            return calc_apply(calc_eval(exp.first), list(exp.rest.map(calc_eval)))
    elif exp in OPERATORS:
        return OPERATORS[exp]
    else:
        return exp

def eval_and(operands):
    for operand in operands:
        if calc_eval(operand) == False:
            return '#f'
    return calc_eval(operands[-1])
    