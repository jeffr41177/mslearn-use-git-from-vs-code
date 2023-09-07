# MANIPULATE LIST DATA

# You might need to work with different portions of a list. For example, assume that you have a list with rainfall amounts for 
# various months. To properly analyze this type of data, you might need to look for rainfall in a three-month period. Or you might 
# want to sort the list in order of most rainfall to least. 
# Python provides robust support for working with the data in lists. 
# This support includes slicing data (examining just a portion) and sorting.

# SLICING a list 
# You can retrieve a portion of a list by using a slice. 
# A slice uses brackets, but instead of a single item, it has the starting # and ending indexes. 
# To use a slice, you create a new list that starts at the starting index and ends before (and does not include) the ending index.
# The list of planets has eight items. Earth is the third in the list. 
# To get the planets before Earth, use a slice to get items starting at 0 and ending at 2:
# WATCH!!!!! If you want items "0 and 1" to be included, set your index to be [0, 2]

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)
# Notice how Earth is not included in the list. The reason is that the index ends before the ending index.

# To get all the planets AFTER Earth, start at the third and go to the eighth:
planets_after_earth = planets[3:8]  # WATCH!!!!  Start with the index/position you want, and add +1 past the last one you want
# print(planets_after_earth)

# Another example
# In the example, Neptune is displayed. The reason is that the index for Neptune is 7, because indexing starts at 0.
# Because the ending index was 8, it includes the last value. 
# If you don't put the stopping index in the slice, Python assumes that you want to go to the end of the list

planets_after_earth = planets[3:]   # This will print planets AFTER Earth, starting with Mars [3] to the end of the list
print(planets_after_earth)
print("\nBEGIN JOIN LISTS SECTION\n")

#  JOIN LISTS
# To join two lists, you use the other operator (+) with two lists to return a new list.
# Create two lists. Populate the first list with the four Amalthea moons and the second list with the four Galilean moons. 
# Join them together by using + to make a new list:
# There are 79 known moons of Jupiter. The four largest are Io, Europa, Ganymede, and Callisto. 
# The Galilean moons, discovered by Galileo using his telescope in 1610 are: Io, Europa, Ganymede, and Callisto. 
# The malthea moons are: Metis, Adrastea, Amalthea, and Thebe.

galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]
amalthea_moons = ["Metis", "Adrastea", "Amalthea", "Thebe"]

regular_satellite_moons = galilean_moons + amalthea_moons  # This is the combined list
print("The combined regular satellite moons of Jupiter (Galilean and Amalthea moons) are", regular_satellite_moons)

# SORT LISTS
# Use the .sort() method
print("\nBEGIN SORT METHOD \n")
regular_satellite_moons.sort()
print("These are the moons sorted using the sort method", regular_satellite_moons)
print("")

# SORT in REVERSE ORDER
regular_satellite_moons.sort(reverse=True)
print("These are moons sorted in reverse order", regular_satellite_moons)
print("")

# BEGIN LIST EXERCISE
print("BEGIN LIST EXERCISE\n")

# Create sting/list of planets
planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets_list)

# Propmt the user to input their refernce planet and store is as 'ref_planet'
ref_planet = input("Enter the reference planet: ")
print("The planet you entered is", ref_planet)

# Use index to find where this ref_planet is in the index
# Create a variable that determines and stores where the ref_planet is in the index
planet_index_posn = planets.index(ref_planet)
print(planet_index_posn)
print("")

# Use a Slice to display all planets that are closer to the sun, up to the one selected
planets_before_ref_planet = planets[0:(planet_index_posn)]
# print("The following planets exist between the sun and your reference planet,", ref_planet, planets_before_ref_planet)
# print("")

# A more efficient way to do this is...
print("Here are the planets closer than " + ref_planet)
print(planets[0:planet_index_posn])

# Display the planet FARTHER from the sun than the reference planet
planets_past_ref_planet = planets[planet_index_posn +1: ]
# offset_planet_posn = planet_index_posn +1
print("Here are the planets farther than your reference planet,", ref_planet, planets_past_ref_planet)
print("")

