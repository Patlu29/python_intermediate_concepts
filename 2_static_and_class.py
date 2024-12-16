class person(object):

    population = 50

    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    @classmethod # you can call it on any instance of a class
    def getpopulation(cls):
        return cls.population
    
    @staticmethod # it can be called without using that class
    def isAdult(age):
        return age >= 18
    
    def display(self):
        print(f"{self.name} is {self.years} old")

newperson = person('patlu', 20)