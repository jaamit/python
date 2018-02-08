'''
Generator - a function that behaves like an iterator, i.e. it can be used in a for loop.

1. The yield statement will make a function generator.
2 . generator object is generated once, but its code is not run all at once. 
Only calls to next actually execute (part of) the code. Execution of the code in a 
generator stops once a yield statement has been reached, upon which it returns a value. 
The next call to next then causes execution to continue in the state in which the 
generator was left after the last yield. This is a fundamental difference with 
regular functions: those always start execution at the "top" and discard their 
state upon returning a value.
https://stackoverflow.com/questions/1756096/understanding-generators-in-python
'''
# Infinite stream

def fib():
...     a, b = 0, 1
...     while True:
...         yield a
...         a, b = b, a + b

import itertools
list(itertools.islice(fib(), 10)) #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
list(itertools.islice(fib(), 15)) #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

def g_n(n):
    for i in range(n):
        yield i

gen = g_n(3)
gen
<generator object g_n at 0x0000018B78E14CA8>
next(gen)
0
next(gen)
1

