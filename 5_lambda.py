"""
a = lambda x: x**2

b = a(int(input("a is: "))) 

c = lambda y: b ** 2

print(c(int(input("b is: "))))

def func(x):
    func2 = lambda x: x+5
    return func2(x)

print(func(2))


func3 = lambda x,y: x**y

print(f"The number is: {func3(int(input("enter a number: ")),int(input("enter a power number: ")))}")
"""

# with map function

a = [y for y in range(1,int(input("Enter how many numbers you want in your list: ")) + 1)]

newList = list(map(lambda x: x ** 2, a))
newList2 = list(filter(lambda x: x%2 == 0,newList))
newList3 = list(filter(lambda x: x%2 != 0, newList))
print(f"Original List is --> {a}")
print(f"New squared list --> {newList}\nThe even list is --> {newList2}\nThe odd List is --> {newList3}")
