# ERROR HANDLING 

# TRACEBACKS
# A traceback is the body of text that can point to the origin (and ending) of an unhandled error. 
# Understanding the components of a traceback will make you more effective when you're fixing errors or debugging
# When a program suffers an unhandled error, a traceback appears as the output.

# open("/path/to/mars.jpg")

# That output has several key parts. First, the traceback mentions the order of the output. Then it informs you that the 
# file is "error.py" on the eigth line of the input. The error is FileNotFoundError 
# (the exception name), which means that the file doesn't exist or perhaps the directory to it doesn't exist.
# It can be hard to understand why line 1 is meaningful or what Errno 2 means

# TRY AND EXCEPT BLOCKS

try:
     open('config.txt')
except FileNotFoundError:
     print('')
     print("Couldn't find the config.txt file!")
     print('')

"""After the try keyword, you can add code that has the potential to cause an exception. Next, you add the except keyword along with the possible exception, followed by any code that needs to run when that condition happens. Because config.txt doesn't exist in the system, Python prints that the configuration file is not there. The try and except block, along with a helpful message, prevents a traceback and still informs the user about the problem.

Although a file that doesn't exist is common, it isn't the only error you might find. Invalid file permissions can prevent reading a file, even if the file exists. Let's create a new Python file called config.py in Visual Studio Code. Add the following code to the file that finds and reads the navigation system's configuration file:
"""   


