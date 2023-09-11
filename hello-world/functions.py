# FUNCTIONS 

def rocket_parts():                             # Define the function that requires no arguments; ends with a colon
    return "payload, propellant, structure"     # Define what the function does; it "returns" the three rocket 
                                                
rocket_parts()                                  # Call (or run) the function
output1 = rocket_parts()                         # Assigns the output of the rocket_parts () to the var output
print('')
print(output1)
print('')

# def str(15):
#     return""
# str(15)
# output2 = str()
# print(output2)

# Calculate Distance from earch using functions with arguments

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

distance_from_earth("Moon")   # Requires an argument to run successfully

# Print the return output for the aurgument entered as the destination
output2 = distance_from_earth("Saturn")
print(f'The distance from the earth to the inputed destination: {output2} miles.')
print('')

# Calculate days to travel to Moon using two arguments
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

# days_to_complete(238855, 75)
# output3 = days_to_complete(238855, 75)
# print(f'The number of days to travel to the Moon at the speed entered: {output3} days.')
# print('')

# Use FUNCTIONS AS ARGUMENTS
total_days = days_to_complete(238855, 75)
output4 = round(total_days)
# output4 = round(total_days)
print(f'The rounded number of days to complete: {output4} days')
print('')

# EXERCISE - ARGUMENTS IN FUNCTIONS

def generate_report(main_tank, external_tank, hydrogen_tank):
    output5 = f"""Fuel Report:
    Main Tank: {main_tank}
    External Tank: {external_tank}
    Hydrogen Tank: {hydrogen_tank}
    """
    print(output5)

generate_report(10, 20, 30)





# print(f'The Main Tank contains: {main_tank} pounds.')
# print(f'The External Tank contains: {external_tank} pounds.')
# print(f'The Hydrogen Tank contains: {hydrogen_tank} pounds.')
