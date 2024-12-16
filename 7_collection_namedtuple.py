import collections
from collections import namedtuple

element = namedtuple('elements','x y z') # it seperate the x y z into variables and assign a set value i given(elements)
# it wil be usable for above example like string, list, tuple, dictionary....
newE = element(1,2,3) # call the element variable and assign the values for x y z 
print(newE) 
print(newE.x, newE.y, newE.z) # it call the elelments by their name
print(newE._asdict()) # it convert newE variable into dictionary
print(newE._fields) # it returns a element name defined inside the namedtuple

# replace
newE = newE._replace(x=4)
print(newE)

# make new one
n2 = element._make(['a','b','c']) # it make a new values for the namedtuple we created first
print(n2)