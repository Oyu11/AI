#! /usr/bin/python3


# ********************************************************
# Name:
# Email address:
# ********************************************************

# This file may be opened in python 3
# Lines beginning with hashes are comments.

# If you are asked to write a procedure, please make sure it has
# the specified name, and the specified number and order of arguments.
# The names of the formal arguments need not be the same
# as in the problem specification.

# For each problem, the intended inputs to your procedures
# are specified (for example, "positive integers")
# and your procedures need not do anything reasonable
# for other possible inputs.

# You may write auxiliary procedures in addition to
# the requested one(s) -- for each of your auxiliary
# procedures, please include a comment explaining
# what it does, and giving an example or two.

# You may also use procedures you have written
# elsewhere in this assignment or previous assignments.
# They only need to be defined once somewhere within this file.

'''
This is meant to get you up to speed with python.

The reading, as needed, includes:

Learning Python
Python Cookbook
Effective Python
and the online Google Python Class

'''

# ********************************************************
# ** problem 0 ** (1 easy point)
# Replace the number 0 in the definition below to indicate
# the number of hours you spent doing this assignment
# Decimal numbers (eg, 6.237) are fine.  Exclude time
# spent reading.

def hours():
    return 5

# ********************************************************
# ********************************************************
# ** problem 1 ** (9 points)
# Write a procedure

# sum_digits(n)

# that takes a positive integer and returns the sum of the digits

# Examples
# sum_digits(13) => 4
# sum_digits(1000000) => 1
# sum_digits(123456789) => 45
# sum_digits(9) => 9

# ********************************************************
# Replace the pass statement with your definition
def sum_digits(n):
    number = str(n)
    sum = 0
    for n in number:
        sum += int(n)
    return sum

# ********************************************************
# ** problem 2 ** (10 points)
# Write a recursive procedure

# reduce(n)

# that takes a positive integer as input, and repeatedly
# sums the digits until the result is less than 10.
# Note: you probably want to call sum_digits from inside reduce

# Examples

# reduce(123455667888) => 9
# reduce(9999) => 9
# reduce(8888) => 5
# reduce(10101010019999) => 5

# ********************************************************
def reduce(n):
    if n < 10:
        return n
    digits = [int(c) for c in list(str(n))]
    return reduce(sum(digits))

# (Replace the pass statement with your procedure(s).)

# ********************************************************
# ** problem 3 ** (10 points)
# Write a procedure

# removep(lst,pred)

# that takes a list lst and returns that list minus
# any elements that satisfy the given predicate pred.

# Examples:

# removep([1,2,3,4,5,6], lambda x: x % 2 == 0) =>[1,3,5]
# removep([1,2,3,4,5,6], lambda x: x % 2) => [2,4,6]
# removep([1,2,3,4,5,6], lambda a: a > 3) => [1,2,3]
# removep([1,2,3,4,5,6], lambda a: a < 3) => [3,4,5,6]

# ********************************************************
def removep(lst, pred):
    # print("hello", [(pred(x)) for x in lst])
    result = []
    for x in lst:
        if pred(x):
            continue
        else:
            result.append(x)

    return result 
# Replace the pass statement with your procedure(s).)

## write the same function using a list comprehansion
def lcremovep(lst, pred):
    result = [x for x in lst if pred(x) == False]
    return result

# ********************************************************
# ** problem 4 ** (10 points)
# Write a procedure

# collectp(lst, pred)

# that takes a list lst and returns that list containing only
# the elements that satisfy the given predicate pred.

# Examples:

# collectp([1,2,3,4,5,6]), lambda x: x%2 == 0) => [2,4,6]
# collectp([1,2,3,4,5,6]), lambda x: x % 2) => [1,3,5]
# collectp([1,2,3,4,5,6]), lambda a: a > 3) => [4,5,6]
# collectp([1,2,3,4,5,6]), lambda a: a < 3) => [1,2]


# ********************************************************

def collectp(lst, pred):
    result = []
    for x in lst:
        if pred(x):
            result.append(x)
        else:
            continue

    return result 

# Replace the pass statement with your procedure(s).)

## write the same function using a list comprehansion
def lccollectp(lst, pred):
    result = [x for x in lst if pred(x) == True]
    return result

# ********************************************************
# ** problem 5 (10 points)
# Write

# power_set(lst)

# which treats the lst as a set and returns a list of all possible
# subsets

'''
Examples:

power_set([]) => [[]]
power_set([1]) => [[], [1]]
power_set([1,2]) => [[], [2], [1], [1,2]]
power_set([1,2,3]) => [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
power_set([1,2,3,4]) =>
[[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 4], [1, 3], [1, 3, 4], [1, 4], [2], [2, 3], [2, 3, 4], [2, 4], [3], [3, 4], [4]]
power_set([2,2]) => [[], [2], [2], [2, 2]]

toppings = ['onion','peppers','bacon','sausage','mushroom']
power_set(toppings) =>

[[], ['bacon'], ['bacon', 'mushroom'], ['bacon', 'sausage'], ['bacon',
'sausage', 'mushroom'], ['mushroom'], ['onion'], ['onion', 'bacon'],
['onion', 'bacon', 'mushroom'], ['onion', 'bacon', 'sausage'],
['onion', 'bacon', 'sausage', 'mushroom'], ['onion', 'mushroom'],
['onion', 'peppers'], ['onion', 'peppers', 'bacon'], ['onion',
'peppers', 'bacon', 'mushroom'], ['onion', 'peppers', 'bacon',
'sausage'], ['onion', 'peppers', 'bacon', 'sausage', 'mushroom'],
['onion', 'peppers', 'mushroom'], ['onion', 'peppers', 'sausage'],
['onion', 'peppers', 'sausage', 'mushroom'], ['onion', 'sausage'],
['onion', 'sausage', 'mushroom'], ['peppers'], ['peppers', 'bacon'],
['peppers', 'bacon', 'mushroom'], ['peppers', 'bacon', 'sausage'],
['peppers', 'bacon', 'sausage', 'mushroom'], ['peppers', 'mushroom'],
['peppers', 'sausage'], ['peppers', 'sausage', 'mushroom'],
['sausage'], ['sausage', 'mushroom']]
''' 

# ********************************************************
## it is OK to use itertools module.
## 
from itertools import *
from tkinter import W

def power_set(lst):
    pw_set = [[]]
    for i in range(0,len(lst)):
        for j in range(0,len(pw_set)):
            ele = pw_set[j].copy()
            ele = ele + [lst[i]]
            pw_set = pw_set + [ele]
    pw_set.sort()
    return pw_set



# ********************************************************
# ** problem 6 ** (10 points)
# Write a procedure

# sumtree(tree)

# that takes a nested list tree and returns the sum of integers in the leaves
# you may NOT assume that all the leaves are integers
# if a leaf is not an integer, ignore it.

# Examples
# sumtree([1, 2, 3]) => 6
# sumtree([1, [2, [3]]]) => 6
# sumtree([[[]]]) => 0
# sumtree([[[[2]]]]) => 2

# sumtree([1,2,3,4]) => 10
# sumtree([1,"2","3",4]) => 5
# sumtree([1,"2","3",4, False]) => 5
# sumtree([1,"2","3",4, False, []]) => 5

# ********************************************************
def sumtree(tree):
    result = 0
    for idx in range(len(tree)):
        if type(tree[idx]) == list:
            result += sumtree(tree[idx])
        elif type(tree[idx]) == int:
            result += tree[idx]
    return result 
# Replace the pass statement with your procedure(s).

# ********************************************************
# ** problem 7 ** (10 points)
# Write a procedure

# doubletree(tree)

# that takes a nested list tree and returns another tree with the same
# structure, but with each element doubled
# you may NOT assume that all the leaves are integers
# if a leaf is not an integer, include it unmodified

# Examples

# doubletree([1, 2, 3]) => [2,4,6]
# doubletree([1, [2, [3]]]) => [2, [4, [6]]]
# doubletree([]) => []
# doubletree([[[[8, 8, 8]]]]) => [[[[16, 16, 16]]]]

# doubletree([1, 2, 3, "4", "5", ["6"]]) => [2, 4, 6, '4', '5', ['6']]
# doubletree([1, 2, 3, "4", "5", ["6"], True]) => [2, 4, 6, '4', '5', ['6'], True]

# ********************************************************

def doubletree(tree):
    result = []
    for idx in tree:
        if type(idx) == list:
            idx = doubletree(idx)
        elif type(idx) == int:
            idx = idx * 2

        result.append(idx)
    return result

# Replace the pass statement with your procedure(s).


# ********************************************************
# ** problem 8 ** (10 points)
# Write a procedure

# types(tree)

# that takes a nested list tree and returns a list of all
# the different data types of the leaf nodes, in alphabetical order,
# without duplication.

# Examples:

# types([1, [2.3, "a"], True, 3, 4, 5]) => ['bool', 'float', 'int', 'str']
# types([1,2,3,4]) => ['int']
# types([1,2,3,4, True, "hello"]) => ['bool', 'int', 'str']
# types([1,2,3,4, True, "hello", 1,2]) => ['bool', 'int', 'str']
# types([1,2,3,4, True, "hello", 1.2]) => ['bool', 'float', 'int', 'str']
# types([1,2,3,4, True, "hello", 1.2, {}]) => ['bool', 'dict', 'float', 'int', 'str']
# types([1,2,3,4, True, "hello", 1.2, {}, (1,2,3)]) => ['bool', 'dict', 'float', 'int', 'str', 'tuple']


# ********************************************************
import re
# pisda juman nested mod shaajishde

def types_helper(tree):
    L = []
    if not(bool(tree)):
        return tree

    if isinstance(tree[0], list):
        return types_helper(*tree[:1]) + types_helper(tree[1:])
 
    resList = tree[:1] + types_helper(tree[1:])   
    return resList 

def types(tree):
    listt = []
    tree = types_helper(tree)
    for idx in tree:
        tmp = str(type(idx)).split()[1]
        tmp = tmp[1:-2]
        listt.append(tmp)
    result = list(set(listt))
    return sorted(result)

# Replace the pass statement with your procedure(s).

## a common use of classes is to implement data structures
## Below is an example of a stack,
## which is a LIFO - last in first out - structure
## it is a collection.
## items are added to the stack with push and removed with pop
## -----------------------------------------------------------
class stack:

    def __init__(self,stuff=[]):
        self.items = stuff[:]
        self.size = len(stuff)

    def __repr__(self):
        return "stack({})".format(list(self.items))

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        self.size += 1

    def peek(self):
        if self.isempty():
            return "Error: stack is empty"
        else:
            return self.items[-1]

    def pop(self):
        if self.isempty():
            return "Error: stack is empty"
        else:
            self.size -= 1
            return self.items.pop()

    ## swap the top two items in the stack
    def rotate(self):
        if self.size < 2:
            return "Error: stack has fewer than 2 elements"
        else:
            self.items[-1], self.items[-2] = self.items[-2], self.items[-1]

    ## define the iterator for stack.  Used in for or list comprehension
    def __iter__(self):
        """Return iterator for the stack."""
        if self.isempty():
            return None
        else:
            index = self.size -1
            while index >= 0:
                yield self.items[index]
                index -= 1

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self.items == other.items:
            return True
        else:
            return False

    # copy constructor - clone the current instance
    def copy(self):
        s = stack(self.items)
        return s

## test the iterator
def itest(s):
    for i in s:
        print (i)
    return [x for x in s]

## revstr uses a stack to reverse a string
## ----------------------------------------
def revstr(str):
    s = stack()
    for c in str:
        s.push(c)
    result = []
    while (not s.isempty()):
        result.append(s.pop())
    return ''.join(result)

# ********************************************************
# ** problem 9 ** (10 points)
#

# Write a procedure balanced(string) that reads string, and determines
# whether its parentheses are "balanced."  Hint: for left delimiters,
# push onto stack; for right delimiters, pop from stack and check
# whether popped element matches right delimiter.

def balanced(string):
    count = 0
    for idx in string:
        if idx == "(":
            count += 1
        elif idx == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0
# ********************************************************
# ** problem 10 ** (10 points)
#

## Write a queue data structure, similar to the stack above.
## Whereas a stack is LIFO (last in first out), a queue is
## FIFO = first in, first out

## See Skiena, page 71

class queue:

    def __init__(self, stuff=[]):
        self.data = stuff[:]
        self.size = len(stuff)

    def __str__(self):
        pass

    def __repr__(self):
        return "queue({})".format(list(self.data))

    def isempty(self):
        return self.data == []

    def enqueue(self, item):
        self.data.append(item)
        self.size += 1

    def dequeue(self):
        if len(self.data) == 0:
            return "queue is empty"
        return self.data.pop(0)
        

    # return error message if queue is empty
    def peek(self):
        if self.isempty():
            return "Error: queue is empty"
        else:
            return self.data[0]

    ## define the iterator for queue.  Used in for or list comprehension
    def __iter__(self):
        """Return iterator for the queue."""
        if self.isempty():
            return None
        else:
            idx = 0
            while idx <= self.size - 1:
                # yield returns generator object 
                yield self.data[idx]
                idx += 1
    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self.data == other.data:
            return True
        else:
            return False

    # copy constructor - clone the current instance
    def copy(self):
        q = queue(self.data)
        return q

# ********************************************************
# ********************************************************
# ********************************************************


### test function from google python course
### =======================================
# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if (hasattr(expected, '__call__')):
        OK = expected(got)
    else:
        OK = (got == expected)
    if OK:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print ('hours')
  print('# is it greater than 0?')
  test(hours(), lambda x: x > 0)

  print ('sum_digits')
  test(sum_digits(10), 1)
  test(sum_digits(13), 4)
  test(sum_digits(1000000),1)
  test(sum_digits(123456789), 45)
  test(sum_digits(9),9)

  print
  print ('reduce')
  test(reduce(123455667888),9)
  test(reduce(9999),9)
  test(reduce(8888),5)
  test(reduce(10101010019999),5)

  print
  print ('removep')
  test(removep(range(7), lambda x: x % 2 == 0),[1,3,5])
  test(removep(range(7), lambda x: x % 2),[0,2,4,6])
  test(removep(range(7), lambda x: x > 3),[0,1,2,3])
  test(removep(range(7), lambda x: x < 3),[3,4,5,6])

  print
  print ('lcremovep')
  test(lcremovep(range(7), lambda x: x % 2 == 0),[1,3,5])
  test(lcremovep(range(7), lambda x: x % 2),[0,2,4,6])
  test(lcremovep(range(7), lambda x: x > 3),[0,1,2,3])
  test(lcremovep(range(7), lambda x: x < 3),[3,4,5,6])

  print
  print ('collectp')
  test(collectp(range(7), lambda x: x % 2 == 0),[0,2,4,6])
  test(collectp(range(7), lambda x: x % 2),[1,3,5])
  test(collectp(range(7), lambda x: x > 3),[4,5,6])
  test(collectp(range(7), lambda x: x < 3),[0,1,2])

  print
  print ('lccollectp')
  test(lccollectp(range(7), lambda x: x % 2 == 0),[0,2,4,6])
  test(lccollectp(range(7), lambda x: x % 2),[1,3,5])
  test(lccollectp(range(7), lambda x: x > 3),[4,5,6])
  test(lccollectp(range(7), lambda x: x < 3),[0,1,2])

  print
  print ('power_set')
  test(power_set([]), [[]])
  test(power_set([1]), [[], [1]])
  test(sorted(power_set([1,2])),
       sorted([[], [2], [1], [1,2]]))
  test(sorted(power_set([1,2,3])),
       sorted([[],[3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]]))
  test(power_set([1,2,3,4]),
       [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 4], [1, 3], [1, 3, 4], [1, 4], [2], [2, 3], [2, 3, 4], [2, 4], [3], [3, 4], [4]])
  test(power_set([2,2]), [[], [2], [2], [2, 2]])

  toppings = ['onion','peppers','bacon','sausage','mushroom']

  test(power_set(toppings),
       [[], ['bacon'], ['bacon', 'mushroom'], ['bacon', 'sausage'], ['bacon', 'sausage', 'mushroom'], ['mushroom'], ['onion'], ['onion', 'bacon'], ['onion', 'bacon', 'mushroom'], ['onion', 'bacon', 'sausage'], ['onion', 'bacon', 'sausage', 'mushroom'], ['onion', 'mushroom'], ['onion', 'peppers'], ['onion', 'peppers', 'bacon'], ['onion', 'peppers', 'bacon', 'mushroom'], ['onion', 'peppers', 'bacon', 'sausage'], ['onion', 'peppers', 'bacon', 'sausage', 'mushroom'], ['onion', 'peppers', 'mushroom'], ['onion', 'peppers', 'sausage'], ['onion', 'peppers', 'sausage', 'mushroom'], ['onion', 'sausage'], ['onion', 'sausage', 'mushroom'], ['peppers'], ['peppers', 'bacon'], ['peppers', 'bacon', 'mushroom'], ['peppers', 'bacon', 'sausage'], ['peppers', 'bacon', 'sausage', 'mushroom'], ['peppers', 'mushroom'], ['peppers', 'sausage'], ['peppers', 'sausage', 'mushroom'], ['sausage'], ['sausage', 'mushroom']])

  print ('sumtree')
  test(sumtree([1, 2, 3]), 6)
  test(sumtree([1, [2, [3]]]), 6)
  test(sumtree([[[]]]), 0)
  test(sumtree([[[[2]]]]), 2)

  test(sumtree([1,2,3,4]), 10)
  test(sumtree([1,"2","3",4]), 5)
  test(sumtree([1,"2","3",4, False]), 5)
  test(sumtree([1,"2","3",4, False, []]), 5)

  print ('doubletree')
  test(doubletree([1, 2, 3]), [2,4,6])
  test(doubletree([1, [2, [3]]]), [2, [4, [6]]])
  test(doubletree([]), [])
  test(doubletree([[[[8, 8, 8]]]]), [[[[16, 16, 16]]]])
  test(doubletree([1, 2, 3, "4", "5", ["6"]]), [2, 4, 6, '4', '5', ['6']])
  test(doubletree([1, 2, 3, "4", "5", ["6"], True]), [2, 4, 6, '4', '5', ['6'], True])

  print ('types')

  test(types([1, [2.3, "a"], True, 3, 4, 5]), ['bool', 'float', 'int', 'str'])
  test(types([1,2,3,4]), ['int'])
  test(types([1,2,3,4, True, "hello"]), ['bool', 'int', 'str'])
  test(types([1,2,3,4, True, "hello", 1,2]), ['bool', 'int', 'str'])
  test(types([1,2,3,4, True, "hello", 1.2]), ['bool', 'float', 'int', 'str'])
  test(types([1,2,3,4, True, "hello", 1.2, {}]), ['bool', 'dict', 'float', 'int', 'str'])
  test(types([1,2,3,4, True, "hello", 1.2, {}, (1,2,3)]), ['bool', 'dict', 'float', 'int', 'str', 'tuple'])
##################

  print ('stack')
  s = stack()
  s.push(1)
  s.push(2)
  s.push(3)
  s.push(4)
  test(s,stack([1, 2, 3, 4]))
  test(s == s.copy(), True)
  test([x for x in s], [4,3,2,1])
  test(s.peek(),4)
  test(3 in s, True)
  test(5 in s, False)
  test(s.pop(),4)
  test(s.pop(),3)
  test(s.peek(),2)
  test(revstr('abcdef'), 'fedcba')
  test(revstr(''), '')

  print ('balanced')

  test(balanced('dkdk'),True)
  test(balanced('()()()()'),True)
  test(balanced('()()()())'),False)
  test(balanced('()()()()(('),False)
  test(balanced('(a)s(d)f(g)gh(h)j(k'),False)

  print ('queue')
  d = queue()
  d.enqueue(9)
  d.enqueue(1)
  d.enqueue(2)
  test(d == d.copy(), True)
  test(d.peek(),9)
  test(d.data,[9, 1, 2])
  test([x for x in d], [9,1,2])
  test(2 in d, True)
  test(5 in d, False)
  test(d.dequeue(),9)
  test(d.dequeue(),1)
  test(d.dequeue(),2)
  test(2 in d, False)
  test(d.dequeue(),'queue is empty')
if __name__ == '__main__':
     main()

