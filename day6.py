
# #Encapsulation 

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self._account_number = account_number
#         self._balance = balance
    
#     def __deposit(self,amount):

#         self._balance += amount
#         print(f"Deposit successful. New Balance : ${self._balance}")


#     def check_balance(self):
#         print(f"Current Balance : {self._balance}")
    
#     def withdraw(self,amount):
#         self._balance -= amount
#         print(f"Wdithdraw successful. New Balance : ${self._balance}")

    
# account = BankAccount('1234',1000)
# # account.deposit(-100)
# # account.withdraw(1500)
# # account.check_balance()

# print(account._account_number)


# class Employee:
#     def __init__(self,name,emp_id,salary):
#         self._name = name 
#         self._emp_id = emp_id
#         self._salary = salary
    
#     def calculate_bonus(self):
#         return self._salary * 0.1
    
#     def display_info(self):
#         print(f"Name : ${self._name}")
#         print(f"Employee id : ${self._emp_id}")
#         print(f"Salary : ${self._salary}")

# employee = Employee('Bob',1,1000)
# employee.display_info()
# bonus = employee.calculate_bonus()

# print(bonus)



# Abstraction 
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width 
    
#     def calculate_perimeter(self):
#        return  2 * (self.length + self.width)
    
#     def get_perimeter(self):
#         return self.calculate_perimeter()
    
# rectangle = Rectangle(1,3)
# perimeter = rectangle.get_perimeter()
# print(perimeter)

#Inheritance 

# class Vehicle:
#     def __init__(self,name,model,year,color):
#         self.name = name 
#         self.model = model 
#         self.year = year
#         self.color = color 
    
#     def display_info(self):
#         print(f"Name : {self.name}")
#         print(f"model : {self.model}")
#         print(f"year : {self.year}")
#         print(f"color : {self.color}")


# class Car(Vehicle):
#     def __init__(self,name,model,year,color,num_doors):
#         super().__init__(name,model,year,color)
#         self.num_doors = num_doors

#     def display_info(self):
#         super().display_info()
#         print(f'Number of doors : {self.num_doors}')

# class Bike(Vehicle):
#     def __init__(self,name,model,year,color,engine_size):
#         super().__init__(name,model,year,color)
#         self.engine_size = engine_size

#     def display_info(self):
#       super().display_info()
#       print(f'Engine Size : {self.engine_size}')


# car = Car('Toyota','thisismodel',2020,'red',4)
# car.display_info()

# bike = Bike('Honda','CBR',2019,'blue',600)
# bike.display_info()


class Employee:
    def __init__(self,name,emp_id):
        self.name = name 
        self.emp_id = emp_id 

    def display_info(self):
        print(f'Name : {self.name}')
        print(f'Employee Id : {self.emp_id}')

class Manger(Employee):
    def __init__(self,name,emp_id,department):
        super().__init__(name,emp_id)
        self.department = department 

    def display_info(self):
         super().display_info()
         print(f'Department : {self.department}')

class Developer(Employee):
    def __init__(self, name, emp_id,programming_lang):
        super().__init__(name, emp_id)
        self.programming_lang = programming_lang

    def display_info(self):
         super().display_info()
         print(f'Programming Language : {self.programming_lang}')


manager = Manger('Bob',1,'engineering')
manager.display_info()

developer = Developer('Pranjal',2,'Javascript')
developer.display_info()