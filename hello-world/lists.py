# This is the List training module

# Create a list of planets using a variable with the list constructed as shown below
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Access the items in the list
# You can access any item in a list by putting the index in brackets [] after the list variable's name. 
# Indexes start from 0, so in the following code, planets[0] is the first item in the list planets:
print("The first (e.g. posn zero) planet is", planets[0])
print("The second (e.g. posn one) planet is", planets[1])
print("The third (e.g. posn two) planet is", planets[2])

# You can also modify values in a list by using an index. 
# You do so by assigning a new value, in much the same way that you would assign a variable value. 
# For example, you could change the name of Mars in the list to use its nickname:
planets[3] = "Red Planet"
print("Mars is also known as the", planets[3])

# Determine the length of a list
# To get the length of a list, use the built-in function len(). 
# The following code creates a new variable, number_of_planets. 
# The code assigns that variable with the number of items in the list planets (8).
number_of_planets = len(planets)
print("The number of planets in this list is", number_of_planets)
print("There are", number_of_planets, "planets in the Solar System, prior to appending Pluto.")

# Append Pluto to the above list
# Lists in Python are dynamic: you can add and remove items after they're created. 
# To add an item to a list, use the method .append(value).
# The following code adds the string "Pluto" to the end of the list of planets:
planets.append("Pluto")
number_of_planets = len(planets)
print("There are a total of", number_of_planets, "planets in the Solar System if you include Pluto.")

# REMOVE VALUES FROM THE LIST  
 # You can remove the last item in a list by calling the .pop() method on the list variable:

planets.pop()  # This removes the 'last' item in the list, which is Pluto
print(planets)  # This displays the list of 8 planets (Pluto is gone from the list)
number_of_planets = len(planets)  # This counts the items in the list as a second confirmation Pluto has been removed
print(number_of_planets)

# USE NEGATIVE INDEXES (From the end of the list forward)
# You can fetch an item from this list by referencing its position
print("The first planet is", planets[0])

# Indexes start at zero and increase. Negative indexes start at the end of the list and work backward.
# In the following example, an index of -1 returns the last item in a list. An index of -2 returns the second to last.
print("The last planet in the list is", planets[-1])
print("The next to the last planet in the list is", planets[-2])
print("The third from the last planet in the list is", planets[-3])
print("The pentultimate (second to last) planet in the list is", planets[-2])

# FIND A VALUE IN A LIST
# To determine where in a list a value is stored, you use the list's index method. 
# This method searches for the value and returns the index of that item in the list. 
# If it doesn't find a match, it returns -1.
# This example shows the use of "Jupiter" as the index value:
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
jupiter_index_posn = planets.index("Jupiter") # Index refers to the numbered position in the list
print("Jupiter is the", jupiter_index_posn + 1, "planet from the sun")   # Add a +1 since indexing begins with posn 0

# Another example of finding a value in a list
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
mercury_index = planets.index("Mercury")
print("Mercury is the", mercury_index + 1, "planet from the sun")  # Add a +1 since indexing begins with posn 0

# EXERCISE - LISTS  

# To store numbers with decimal places in Python, you use the float type. 
# To create a float, you enter the number with the decimal place and assign it to a variable:
gravity_on_earth = 1.0
gravity_on_the_moon = 0.166

# The following code creates a list that shows the gravitational forces of all 8 planets in the solar system, in G:
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

# Above, gravity_on_planets[0] is gravity on Mercury (0.378 G), gravity_on_planets[1] is gravity on Venus (0.907 G), and so on. 
# On Earth, a double-decker bus weighs 124,054 Newtons (N). 
# On Mercury, where the gravity is 0.378 G, the same bus weighs 124,054 Newtons multiplied by 0.378. 
# In Python, to multiply two values, you use the * symbol. 
# In example below, you can work out the weight of a double-decker bus on different planets by getting the value from the list:

gravity_on_mercury = gravity_on_planets[0]
gravity_on_venus = gravity_on_planets[1]
gravity_on_earth = gravity_on_planets[2]
gravity_on_mars = gravity_on_planets[3]
gravity_on_jupiter = gravity_on_planets[4]
gravity_on_saturn = gravity_on_planets[5]
gravity_on_uranus =  gravity_on_planets[6]
gravity_on_neptune =  gravity_on_planets[7]

print(gravity_on_mercury)
print(gravity_on_venus)
print(gravity_on_earth)
print(gravity_on_mars)
print(gravity_on_jupiter)
print(gravity_on_saturn)
print(gravity_on_uranus)
print(gravity_on_neptune)

# gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "N")

# USE MIN AND MAX 
# gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
# bus_weight = 12650 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")
