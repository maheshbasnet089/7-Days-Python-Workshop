
# def add(a,b):
#    return a + b 

# result = add(1,2)
# print(result)

# class Calculation:
#     def add(self,a,b):
#      return a + b
    
# calculator = Calculation()
# bob_ko_calculator = Calculation()
# result2 = calculator.add(1,2)
# print(result2)


class Animal:
    
    def __init__(self,name):
        self.__name = name 
    
    def eat(self):
        print(self.__name)
        print("I can eat")
    
    def sleep(self):
        print("I can sleep")

class Dog(Animal):
    def bark(self):
        print(" I can bark")

dog1 = Dog('German Shepherd')
# print(dog1.__name)
dog1.eat()
# dog1.sleep()


# dog2 = Dog('Dog2 here')
# dog2.bark()




    
