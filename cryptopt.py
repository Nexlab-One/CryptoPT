#####################################
# Crypto Portfolio Tracker          #
# Enoch Kuskoff -> ZeroSource.io    #
# 11/04/2023                        #
#####################################

# Imports
import sys
from args import checkArguments
from show import show
from save import save

# Main Instance of Program
if __name__=="__main__":
    argument = checkArguments() # Check to ensure that valid and correct amount of arguments were supplied.
    
    if argument is not None:
        match sys.argv[1]: # Match first argument to relevant method and call it.
            case "save":
                save(sys.argv[2], sys.argv[3]) # Pass following arguments to save method.
            case "show":
                show(sys.argv[2], sys.argv[3]) # Pass following arguments to save method.
    else:
        exit()