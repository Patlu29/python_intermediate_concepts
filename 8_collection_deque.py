import collections
from collections import deque

## deque is fast for adding a element begining and end of the list

d = deque("hello")
print(d)

d.append(4) # append in the end of the list 
d.appendleft(5) # append in the left end of the list 
print(d)

d.pop() # remove or pop the last element of the list or which index we want to remove
d.popleft() # removes the first element on the list 
print(d)