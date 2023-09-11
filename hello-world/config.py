def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


if __name__ == '__main__':
    main()

"""When errors are of a similar nature and there's no need to handle them individually, you can group the exceptions together as one by using parentheses in the except line. For example, if the navigation system is under heavy loads and the file system becomes too busy, it makes sense to catch BlockingIOError and TimeOutError together: (see above)
If you need to access the error that's associated with the exception, you must update the except line to include the as keyword. This technique is handy if an exception is too generic and the error message can be useful:
"""
try:
    open("mars.jpg")
except FileNotFoundError as err:
     print("Got a problem trying to read the file:", err)  # This prints the error with the specific exception

try:
    open("config.txt")
except OSError as err:
     if err.errno == 2:
         print("Couldn't find the config.txt file!")
     elif err.errno == 13:
        print("Found config.txt but couldn't read it")

