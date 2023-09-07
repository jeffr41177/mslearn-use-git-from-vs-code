# LOOP Section

# user_input = ''

# while user_input.lower() != 'done':
#     user_input = input('Enter a new value, or done when done')
#     print(user_input)

# A more robust while loop with data entry

# Create the variable for user input
user_input = ''

# Create a list to store/append all of the values from user_input
inputs_list = []

# The while loop
while user_input.lower() != 'done':
    # Check if there's a value in user_input
    if user_input:   # if user_input is true, meaning it has a value
        # Store the value in the list
        inputs_list.append(user_input)
    # Prompt for a new value
    user_input = input('Enter a new value, or "done" when finished: ') # Prompt for input and store in user_input variable or end 

print(inputs_list)

# WHILE LOOP EXERCISE 
print("\nBEGIN WHILE LOOP EXERCISE\n")

new_planet_input = ''

planets_list = []

while new_planet_input.lower() != 'done':
    if new_planet_input:
        planets_list.append(new_planet_input)
    new_planet_input = input('Enter a new planet, or "done" when finished: ')

print(planets_list)
print('')

