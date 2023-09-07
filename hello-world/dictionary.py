# DICTIONARY section

# Create a dictionary to store the name of the planet and the number of moons (in the KEYS "name" and "moons")
planet = {
    'name': 'Earth',    # name is a KEY
    'moons': 1          # moons is a KEY
}

# PRINT THE KEYS AND VALUES
print(planet.get('name'))
print(planet.get('moons'))

# A MORE EFFECIIENT METHOD
print('')
print(planet['name'])
print(planet['moons'])

# USING .GET WILL 'NOT'RETURN AN ERROR IF NO DATA IS FOUND (it returns NONE); THE EFFICIENT METHOD WILL RETURN AN ERROR
# wibble = planet.get('wibble')      # Returns None
# print(wibble)

wibble = planet['wibble']            # Throws KeyError
print(wibble)

# MODIFY DICTIONARY VALUES

planet.update({'name': 'Makemake'})   # No output: name is now set to Makemake.
planet['name'] = 'Makemake'           # No output: name is now set to Makemake.

# This is the more EFFICIENT WAY TO MAKE MULTIPLE UPDATES (using one function call) to the DICTIONARY
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# THIS CAN ALSO BE USED TO MAKE MULTIPLE UPDATES TO THE DICTIONARY
planet['name'] = 'Jupiter'
planet['moons'] = 79
