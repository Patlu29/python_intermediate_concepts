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

# extend method in deque
for i in range(1,10,2):
    d.extend(f"{i}") # it addd the element and extend the list at the end
print(d)

# extendleft method
for i in range(2,10,2):
    d.extendleft(f"{i}")
print(d)

# rotate the deque
d.rotate(-1) # if i give (-) numbers it moves the element left side
print(f"left moved deque: {d}")

d.rotate(2) # if i give the (+) numbers it moves the elements right side
print(f"right moved deque: {d}")