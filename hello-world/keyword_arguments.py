# USING KEYWORD ARGUMENTS IN FUNCTIONS

# Optional arguments require a default value assigned to them. These named arguments are called keyword arguments. 
# Keyword argument values must be defined in the functions themselves. 
# When you're calling a function that's defined with keyword arguments, it isn't necessary to use them at all.
# The Apollo 11 mission took about 51 hours to get to the Moon. 
# Let's create a function that returns the estimated time of arrival by using the same value as Apollo 11 mission as the default:

# The function uses the datetime module to define the current time. 
# It uses timedelta to allow the addition operation that results in a new time object. 
# After computing that result, it returns the arrival estimation formatted as a string. 
# IF called without any arguments, 

from datetime import timedelta, datetime

def arrival_time(destination, hours=48):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination}: Arrival Estimate: %A %H:%M")

# Call the function with the default value (51 hours in the future)
default_arrival = arrival_time("Moon", 48)

print('')
print(f'The default arrival time using the inputted 48 hours is: {default_arrival}')

# Call the function with a custom number of hours (e.g., 24 hours in the future)
custom_arrival = arrival_time("Moon", 24)
print('')
print(f'The custom arrival time of 24 hours in the future is: {custom_arrival}')
print('')

# MIXED ARGUMENTS AND KEYWORD ARGUMENTS (above - added 'destination')
# Sometimes, a function needs a combination of arguments and keyword arguments. 
# In Python, this combination follows a specific order. Arguments are always declared first, followed by keyword arguments.
# Update the arrival_time() function to take a required argument, which is the name of the destination:
# Because you added a required argument, it's no longer possible to call the function without any arguments: