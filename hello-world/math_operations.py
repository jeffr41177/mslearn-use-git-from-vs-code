# Addition
answer = 30 + 12
print(answer)

# # Subtraction
difference = 30 - 12
print(difference)

# # Multiplication
product = 30 * 12
print(product)

# # Division
quotient = 30 / 12
print(quotient)

# Convert seconds to minutes
# The first step is to determine the number of minutes in 1042 seconds. With 60 seconds in a minute, you can divide by 60 and get an answer of 17.3666667. The number you're interested in is simply 17. You always want to round down, by using what's known as floor division. To perform floor division in Python, you use // (to just display the whole number of seconds).
seconds = 1042
display_minutes = 1042 // 60
print(display_minutes)

# The next step is to determine the number of seconds. This number is the remainder of 1042 if you divide by 60. You can find the remainder by using the modulo operator, which is % in Python. The remainder of 1042 / 60 is 22, which is what the modulo operator will provide.
seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

# # Math Order of Operations: 1) Parenthesis 2) Exponents 3) Mult & Division 4) Add & Subtract
result_1 = 1032 + 26 * 2
print(result_1)

result_2 = 1032 + (26 * 2)
print(result_2)

print("BEGIN EXERCISE\n")

first_planet = 149597870
second_planet = 778547200
print(first_planet)
print(second_planet)

distance_km = second_planet - first_planet
print(distance_km)

distance_miles = distance_km / 1.609344
print(distance_miles)

# Convert Strings to Numbers
print("\nConvert Strings to Numbers\n")

# Python supports two main types of numbers: integers (or int) and floating point (or float).
# When you're converting strings to numbers, you indicate the type of number you want to create. You must decide if you need a decimal point. You use int to convert to an integer, and float to convert to a floating point number.

demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

print("\nAbsolute Values")
# An absolute value in math is the non-negative number without its sign. Using an absolute value can be useful in different situations, including our example of looking to determine distance between two planets. Consider the following math
print(39 - 16)
print(16 - 39)

# Convert to abs
print("\nConvert to abs")
print(abs(39 - 16))
print(abs(16 - 39))

# Rounding
print("\nRounding")
print(round(14.5))

# Math Library
print("\nMath Library")
# Python has libraries to provide more advanced operations and calculations. One of the most common is the math library. math allows you to perform rounding with floor and ceil, provide the value of pi, and numerous other operations. Let's see how to use this library for rounding up or down.

# Rounding numbers enables you to remove the decimal portion of a float. You can choose to always round up to the nearest whole number by using ceil, or down by using floor. ROUND UP by using ceil; ROUND DOWN by using floor.

from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

# Calculate distance to planets
first_planet_input = input('Enter the distance from the sun for the first planet in km:  ')
second_planet_input = input('Enter the distance from the sun for the second planet in km:  ')

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

print(first_planet)
print(second_planet)

distance = abs(second_planet - first_planet)
print(abs(distance))





