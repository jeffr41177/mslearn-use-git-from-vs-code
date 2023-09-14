# Create the variable strPath to hold the filename text.txt
strPath = "data/text.txt"

# Use the open() function to create the file in Python. 
# Make a new variable named fileObject to hold the data. 
# Open the file with var strPath with Write (create/overwrite) privs and assign to fileObject
fileObject = open(strPath, "w")

# Write two statements to the file
fileObject.write("The First Astronaut on the moon was:\n")
fileObject.write("Neil Armstrong\n")

# Close the file; this flushes any data that hasn't been written to the file on disk yet.
fileObject.close()

# Open the file after it has been written to with no privs => Read Only, so we can READ from it
fileObject = open(strPath)

# Read each of the lines in the fileObject variable and assign it to textList
# Read this fileObject variable to give us a list of strings that we can explore using readlines() function. 
# The readlines() function takes each line of the text file and makes it an entry in a list. 
# We'll store this list in another variable textList so we can print it out later. 
# It's also good practice to close the fileObject when you're done with it. 

textList = fileObject.readlines()
fileObject.close()

# For each line in textList variable, print line
for line in textList:
    print(line)

# Read the first line of the textList variable, assign it to firstLine, then print firstLine
firstLine = textList[0]
print(firstLine)

# Read the second line of the textList variable, assign it to secondLine, then print secondLine
secondLine = textList[1]
print(secondLine)
