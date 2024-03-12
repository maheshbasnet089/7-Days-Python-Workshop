
#name--> parameter(incoming data accept garney placeholder)
# def greet(name):
#     print(f"Hello,{name} ")

# greet('Anup')
# greet("bob")


#write a function to add 2 number
# def addition(a,b):
#     sum= a+b
#     print("The sum is:", sum)

# addition(1,4)

# def add(a,b):
#     print(a+b);

# add(5,6)


# def add_numbers(num1, num2):
#     return num1 + num2
    
# result = add_numbers(5, 7)
# print("The sum is:", result)

# add = lambda a,b : a + b
# multiply = lambda x,y : x*y

# print(add(1,2))
# print(multiply(1,2))

def test(*args):
    print(args)

test(1,2,3)

def is_even(number):
    return number % 2 == 0

result = is_even(5)
print(result)

