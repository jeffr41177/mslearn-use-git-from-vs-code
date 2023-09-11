# From the Python book

def welcome():
    print("Good Morning! I hope you are well.")

welcome()

# A second example usng a docstring (which is triple quotes for longer commenting)

def myFunction():
    """
    Author: Jeff Ross
    Function:  MyFunction to do xyz
    Purpose: Print a greeting!
    """
    print("Hi! I wish you a good day!")

myFunction()

# Example function with a single parameter

def greet_user(name):
    print('')
    print("Hi " + name + ", I hope you are well!")

greet_user('Jane')
greet_user('Bill')
greet_user('Jake')
greet_user('Sam')
print('')

# Positional arguments

def age(who, years):
    print(who, "is", years, "years old.")

age('Tom', 20)
age("Mike", 10)
print('')

# Keyword Arguments - overcome the issues with positional integrity of positional arguments
# With Keyword arguments, we can pass arguments to function parameters using the format: parameter = value 

def age_kw(who, years):
    print(who, "is", years, "years old.")
    print('')
    
age_kw(who = 'James', years = 30)
age_kw(who = "Thomas", years = 40)

# EXCEPTION HANDLING    

def divide32(x):
    try:
        result = 32 / x
        print(result)
    except ZeroDivisionError:
        print("User Error: You can't divide by zero.")

divide32(8)
divide32(0)
divide32(3.2)


