# Crypto Portfolio Tracker

# Imports
import sys

# Functions
def checkArguments(): # https://www.cyberciti.biz/faq/python-command-line-arguments-argv-example/
    # Return Message if too many arguments are passed
    if len(sys.argv) > 2: 
        print("Too many arguments")
        return None
    elif len(sys.argv) < 2:
        print("Please supply an argument")
        return None

    argsList = str(sys.argv) # Get the arguments list 

    return argsList



# Main Instance of Program
if __name__=="__main__":
    argument = checkArguments()
    if argument is not None:
        print(argument)
    else:
        exit()
    
