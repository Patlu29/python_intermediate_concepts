'''
def func(x=1): # if i dont pass the value it print the default value 1 but when i pass it take that as a parameter 
    # it is called optional parameter
    return x ** 2 

call = func(5)
print(call)

# optional parameter in string

def fun (x, y=1):
    return x*y
call = fun("hii patlu--",5)
print(call)
'''

# with a class 

class car (object):
    def __init__(self,make,model,year,condition,kms):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms
    
    def display(self, showall):
        if showall:
            print("this car is a %s %s from %s, it is %s and has %s kms." %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This is a %s %s from %s." %(self.make, self.model, self.year))

rr = car('rolls royse', 'desert eagle', 2023, 'New', 240)
rr.display(False)
