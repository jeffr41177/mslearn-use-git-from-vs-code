# Calculate moons exercise - Dictionary values

planet_moons = {
    'mercury' : 0,
    'venus' : 0,
    'earth' : 1,
    'mars' : 2,
    'jupiter' : 79,
    'saturn' : 82,
    'uranus' : 27,
    'neptune' : 14,
    'pluto' : 5,
    'haumea' : 2,
    'makemake' : 1,
    'eris' : 1
}

print(f'The number of moons of Pluto is: {planet_moons["pluto"]}')    # Print to confirm dictionary works correctly
#print(f'{planet_moons["name"]} has {planet_moons["moons"]} moons.')

# Determine the number of moons using the len() method
#print('')

#moons = len(planet_moons)
#print(f'The total number of moons is {moons}.')

# print('')

# Obtain a list of all the moons using the values() method

#moons = planet_moons.values() 
# print(f'{moons}')

# print('')

# Determine the number of moons using the len() method
# print('')

# Obtain a count of all the moons using the len() method
#total_planets = len(planet_moons)
#print(f'The total number of planets is {total_planets}.')

# print('')


# Text book answers below, give the same result as mine above, which is only 12 dictionary entries (12 planets)
# # THis is NOT the total number of moons
# moons = planet_moons.values()    # This is a list of the dictionary values with the number of moons for each planet
# total_planets = len(planet_moons.keys())        # This is the total number of planets (not moons)

# print(f'The quantity of moons is: {moons}')
# print(f'The quantity of planets is {total_planets}')

print('')

moons = planet_moons.values()   # Use the values() method to list the dicty values of planet_moons dict and store in var moons
total_planets = len(planet_moons.keys())    # Determine the number items/keys/planets in dict to calc avg # moons per planet


print(f'The dictionary values using the value() method is: {moons}.')
print(total_planets)
print('')



# Determine the TOTAL NUMBER OF MOONS and AVERAGE number of moons

total_moons = 0

for each in moons:
    total_moons = total_moons + each
print(f'{total_moons}')

average = total_moons / total_planets

print(f'The average number of moons is: {average}.')
print('')




