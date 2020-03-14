## Problem
Determine whether an one-to-one character mapping exists from one string, s1, to another string, s2.

## Examples
* abc -> bcd, *true*
* foo -> bar, *false*
* bar -> foo, *true*
  
## Key idea
Since the length of the strings are the same, we allocate a unique number to each mapping, which leads to a unique equivalent overall summation for strings that can be transformed.   
For example,
* abc -> bcd, a <-> b = 1, b <-> c = 2, c <-> d = 3, so return *true*.
* foo -> bar, f <-> b = 1, o <-> a = 2, o <-> r can not be assigned an integer, because 'o' has already be assigned 2. Return *false*.
* bar -> foo, b <-> f = 1, a <-> o = 2, r <-> o = 3, so return *true*.
