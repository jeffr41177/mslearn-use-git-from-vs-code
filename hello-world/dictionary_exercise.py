# # Dictionary Exercise
print('')

# #  Create a variable named planet. Store the following values as a dictionary:
planet = {
    'name' : 'Mars',
    'moons' : '2'
}
print(f'{planet["name"]} has {planet["moons"]} moons.')

planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
print(f'The planet {planet["name"]} has a {planet["circumference (km)"]["polar"]} km polar circumference and an equatorial circumference of {planet["circumference (km)"]["equatorial"]} km.')
print(f'{planet["circumference (km)"]["equatorial"]}.')

print('')

# Exercise RETRIEVEING ALL KEYS and VALUES

# Create a dictionary with the last three months of rainfall
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

print(f'The rainfall for october was {rainfall["october"]} cm.')

# Use the KEYS() METHOD to return a list object that contains all the keys.
# You can use the KEYS() method to iterate through all items in the dictionary.

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]} cm')

print('')
# Use IN to determine if a key exists, and if it does exist, then increment it

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1      # Because december exists, the value will be 3.1

print(f'The incremented value for december is {rainfall["december"]} cm.')

print('')

# Exercise RETRIEVE all Values

# Similar to keys(), the values() method returns the list of all values in a dictionary without their respective keys. 
# The values() method can be helpful when you're using the key for labeling purposes, such as the preceding example, in which the keys are the name of the month. 
# You can use the values() method to determine the total rainfall amount:

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was a total rainfall of {total_rainfall} cm in the last quarter.')

print('')





