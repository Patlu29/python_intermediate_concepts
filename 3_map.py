# normal way

li = [1,2,3,4,5,6,7,8,9]

def func(x):
    return x**x

newli = []
for x in li:
    newli.append(func(x))

print(newli)

# with map function

print(list(map(func, li))) # in this method map function do the work of iterate the list(li) elements through the function
