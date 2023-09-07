# FOR Loops

from time import sleep

countdown = [4, 3, 2, 1, 0]
for number in countdown:
    # sleep(1)
    print(number)
print("Blast off!! 🚀")

# WHILE and FOR LOOP EXERCISE 
print("\nBEGIN WHILE LOOP EXERCISE\n")

# This is the WHILE loop
new_planet_input = ''

planets_list = []

while new_planet_input.lower() != 'done':
    if new_planet_input:
        planets_list.append(new_planet_input)
    new_planet_input = input('Enter a new planet, or "done" when finished: ')

print(planets_list)
print('')

# This is a FOR loop to print the output until all Planets entered have been printed
for new_planet_input in planets_list:
    print(new_planet_input)
    print('')
