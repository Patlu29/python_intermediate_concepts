def add5(x):
    return x + 5

def odd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,10]

b = list(map(add5, a))

c = list(filter(odd, a))

print(f"a is: {a}\nadd 5 with a is:{b} ")

print(f"a is: {a}\nodd numbers: {c}")