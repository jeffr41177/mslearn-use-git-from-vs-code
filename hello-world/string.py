# String Operations

# fact = "The moon has no atmosphere. "
# second_fact = fact + "There is no sound on the moon."
# print(second_fact)

# fact3 = "The moon has a radius of 1,080 miles." 
# print (fact3)

# fact4 = 'The "near side" is the part of the Moon that faces the Earth.'
# print(fact4)

# sum_facts = second_fact + '\nThe moon has a radius of 1,080 miles. The "near side" is the part of the Moon that faces the Earth.'
# print(sum_facts)

# fact5 = """We only see about 60% of the Moon's surface."""
# print(fact5)

# # Multiline Text Output
# multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
# print(multiline)

# Another multiline option using """
# multiline2 = """Facts about the Moon: 
#  There is no atmosphere. 
#  There is no sound."""
# print(multiline2)

# Use string methods for format strings. These methods exist as string variables and are part of the string itself.
# print("temperatures and facts about the moon".title())  # Prints the string as a title with Capitalization

# heading = "more facts about moon temperatures"  # Another way to create a title using string methods
# heading_upper = heading.title()
# print(heading_upper)

# Split a String 
# temperatures = "Daylight: 260 F Nighttime: -280 F"
# temperatures_list = temperatures .split()
# print(temperatures_list)

# Split a String with new lines (\n "new line" is merely the delimiter, not an actual new line)
# temperatures = "Daylight: 260 F \n Nighttime: -280 F"
# temperatures_list = temperatures.split('\n')
# print(temperatures_list)

# Search String Methods
# # Find the word "Moon" (return "False" if the word is not found; "True" if the word is found)
# print("Moon" in "This text will describe facts and challenges with space travel")
# print("Moon" in "This text will describe facts about the Moon and challenges with space travel")

# find returns a -1 if the value is not found and the index (position number of the preceding space) if it is found
# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
# print(temperatures.find("Moon"))

# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
# print(temperatures.find("Mars"))

# .count provides the number of times the search word is found in the string
# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
# print(temperatures.count("has"))
# print(temperatures.count("Moon"))
# print(temperatures.count("Mars"))

# # Convert string to lower case and then upper case
# print("The Moon And The Earth".lower())
# print("The Moon And The Earth".upper())

# Check content of a string
# To extract the avg temp on Mars, use this. The preceding code trusts that everything after the colon (:) is a temperature. 
# The string is split at :, which produces a list of two items. Using [-1] on the list returns the last item, 
# which is the temperature in this example.
# temperatures = "Mars Average Temperature: -60 C"
# parts = temperatures.split(':')
# print(parts)   # print the parts using a comma to separate at the split (defined by the colon)
# print(parts[-1])  # -1 returns the last item in the split list


# If the text is irregular, you can't use the same splitting methods to get the value. 
# You must loop over the items and check to see whether the values are of a certain type. 
# Python has methods that help check the type of string:
# mars_temperature = "The highest temperature on Mars is about 30 C"
# for item in mars_temperature.split():
#     if item.isnumeric():
#         print(item)
# # Like the .isnumeric() method, .isdecimal() can check for strings that look like decimals.

#  # There are extra validations that you can apply on strings to check for values. 
#  # For negative numbers, the dash is prefixed to the number, and that can be detected with the .startswith() method:
# mars_temperature = "The highest temperature on Mars is about 30 C"
# print("-60".startswith('-'))

# Similarly, the .endswith() method helps with verifying the last character of a string:
# mars_temperature = "The highest temperature on Mars is about 30 C"
# if "30 C".endswith("C"):
#     print("This temperature is in Celsius")

# # You can use the .replace() method to find and replace occurrences of a character or group of characters:
# print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))
# # As mentioned earlier, .lower() is a good way to normalize text to do a case-insensitive search. 
# # Let's quickly check to see whether some text discusses temperatures:
# text = "Temperatures on the Moon can vary wildly."
# print("temperatures" in text) # returns false if the string in proper case is not found (here it is not found); true if it is found
# text = "Temperatures on the Moon can vary wildly."
# print("temperatures" in text.lower())  # We must convert the text to lower case, and it DOES find "Temperature"

# You might not need to do case-insensitive verification all the time, but lowercasing every letter is a good approach 
# when the text uses mixed casing.
# After you've split the text and performed the transformations, you might need to put all the parts back together again.
# Just as the .split() method can separate characters, the .join() method can put them back together.
# In this example, ' ' is used to join every item in the list.
# moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
# print(moon_facts)
# print(' '.join(moon_facts))


# Begin String EXERCISE (Use TRIPLE QUOTES to declare multiline string)
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
# print(text)
sentences = text.split('. ')
#print(sentences)
# print(sentences.find("temperature"))
for sentence in sentences:
    #if sentence.find("temperature"):  # this does not work
    if "temperature" in sentence:
       print(sentence)