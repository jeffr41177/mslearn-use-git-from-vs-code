# Percent Sign Formatting
# The placeholder for the variable in the string is %s. After the string, use another % character followed by the variable name. The following example shows how to format by using the % character:
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)

# Using multiple values changes the syntax, because it requires parentheses to surround the variables that are passed in:
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
# The above method is not the best for doing this; Try one of the below that should be better

# The format() method
# The .format() method uses braces ({}) as placeholders within a string, and it uses variable assignment for replacing text.
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))

# Instead of empty braces, the substitution is to use numbers. The {0} means to use the first (index of zero) argument to .format (), which in this case is Moon. For simple repetition {0} works well, but it reduces readability. To improve readability, use keyword arguments in .format() and then reference the same arguments within braces:
mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))


# Use f-strings
#  As of Python version 3.6, it's possible to use f-strings. These strings look like templates and use the variable names from your code. Using f-strings in the preceding example would look like this:
# The variables go within braces, and the string must use the f prefix.
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

# Aside from f-strings being less verbose than any other formatting option, it's possible to use expressions within the braces. These expressions can be functions or direct operations. For example, if you want to represent the 1/6 value as a percentage with one decimal place, you can use the round() function directly:
print(round(100/6, 1))

# With f-strings, you don't need to assign a value to a variable beforehand:
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

# Using an expression doesn't require a function call. Any of the string methods are valid as well. For example, the string could enforce a specific casing for creating a heading:
subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)

print("BEGIN Format Strings EXERCISE BELOW \n")

name = "Ganymede"
planet = "Mars"
gravity = "1.43"

subject = "gravity facts about {name}" 
##print(subject)
#heading = f"{subject.title()}"
#print(heading)

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template.format(name=name, planet=planet, gravity=gravity))
