# VARIABLE ARGUMENTS

# In Python, you can use any number of arguments and keyword arguments without declaring each one of them. 
# This ability is useful when a function might get an unknown number of inputs.
# Arguments in functions are required. But when you're using variable arguments, the function allows any number of 
# arguments # (including 0) to be passed in. 
# The syntax for using variable arguments is prefixing a single asterisk (*) before the argument's name.
# It isn't required to call variable arguments args. You can use any valid variable name. 
# Although it's common to see *args or *a, you should try to use the same convention throughout a project.
# In this case, *args is instructing the function to accept any number of arguments (including 0). 
# Within the function, args is now available as the variable that holds all arguments as a tuple. 
# Try out the function by passing any number or type of arguments:

# def variable_length(*args):
#     print(args)

# variable_length()
# ()
# variable_length("one", "two")
# ('one', 'two')
# variable_length(None)
# (None,)


# A rocket ship goes through several steps before a launch. 
# Depending on tasks or delays, these steps might take longer than planned. 
# Create a variable-length function that can calc how many minutes until launch, given how much time each step is going to take:
# When you use variable arguments, each value is no longer assigned a variable name. 
# All values are now part of the catch-all variable name that uses the asterisk (args in these examples).

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

return_value=sequence_time(20, 20, 26)       #  This calls the function with inputted args, and stores the result for printing
print(return_value)
print('')

# VARIABLE KEYWORD ARGUMENTS    

# For a function to accept ANY NUMBER OF KEYWORD ARGUMENTS, a DOUBLE ASTERICK is required:

def variable_length(**kwargs):
    print(kwargs)
    print('')

variable_length(tanks=1, day="Wednesday", pilots=3)
{'tanks': 1, 'day': 'Wednesday', 'pilots': 3}

# Notice that variable-length keyword arguments are assigned as a dictionary (above). 
# To interact with the variables and values, use the same operations as a dictionary.
# As with variable arguments, you're not required to use kwargs when you're using variable keyword arguments (above). 
# You can use any valid variable name. 
# Although it's common to see **kwargs or **kw, you should try to use the same convention throughout a project.

# ANOTHER EXAMPLE BELOW
# In this function, let's use variable keyword arguments to report the astronauts assigned to the mission. 
# Because this function allows any number of keyword arguments, it can be reused regardless of the number of astronauts assigned:

def crew_members(**kwargs2):
    print(f"There were {len(kwargs2)} astronauts assigned to this mission:")
    for title, name in kwargs2.items():
        print(f"{title}: {name}")


crew_members(Commander="Neil Armstrong", Lunar_Module_Pilot="Buzz Aldrin", Command_Module_Pilot="Michael Collins")

# Note: Because you can pass any combination of keyword arguments, make sure to AVOID REPEATED KEYWORDS as arguments.
# Repeated keywords as arguments result in an ERROR:
 #This code will cause error:
# crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", pilot="Michael Collins")
# File "<stdin>", line 1
# SyntaxError: keyword argument repeated: pilot

#  EXERCISE: KEYWORD ARGUMENTS in functions

# In the prior exercise you created a report for a ship with three fuel tanks. What happens if the ship has multiple tanks? 
# Keyword arguments can be a perfect solution for this type of a situation. 
# With keyword arguments, a caller can provide multiple values which your code can interact with.
# Create a new function named fuel_report. The function will accept a keyword arguments parameter named fuel_tanks. 
# Add the code to loop through the entries provided to generate the following output, where name is the name of the keyword 
# argument and value is the value:

def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():      # accept keyword arguments using **fuel_tanks; iterate through theM using .items()
        print(f'{name}: {value}')               # Print the name and value of each keyword argument (the quanity can vary)

print('')
fuel_report(Main = 100, External = 200, Hydrogen = 300)
print('')


