import collections
from collections import Counter

"""
counter is a method that counts how many times a single element repeated in the container
container is nothing but (list,dictionary,tuple,set)
"""

"""
c = Counter("banana")
print(c)
d = Counter(['a','b','c','a','c'])
print(d)
e = Counter({'a':1,'b':2,'c':5}) # in dictionary Counter returns a highest value key order
print(e)
f = Counter(ak = 5, pk = 7, dk = 10, sk = 2,uk = 10)
print(f)
# print elements in the Counter
print(list(f.elements())) # it return each and every element by their value...ex: ak = 5 --> ak,ak,ak,ak,ak
# print most common elements
print(f.most_common(2))
"""
# subtract
"""
c = Counter(a = 4, b = 3, d = 2, c = -1)
d = ['a','a','b','c','d']
print(f"Original counter: {c}")
c.subtract(d)
print(f"subtracted counter c from d: {c}")
"""
# update --> additon
"""
c = Counter(a = 1, b = 2, c = 2, d = 3)
d = ['a','a','b','c','d','d']
print(f"before update: {c}")
c.update(d)
print(f"after update: {c}")
# use c.clear() to clear all the elements
"""

c = Counter(a = 4, b = 2, c = 0, d = -2)
d = Counter(['a','b','b','c'])

print(f"Union: {c | d}") # it returns union
print(f"Intersection: {c & d}") # it returns intersection