#####################################
# Crypto Portfolio Tracker          #
# Enoch Kuskoff -> ZeroSource.io    #
# 11/04/2023                        #
#####################################

# Imports
import os, os.path, sys, json

# Variables
saveArg = """save [portfolio_name] [Crypto_Ticker]=[Amount_with_Decimal]
         ^ - The "save" argument creates or overwites an existing portfolio identified by the unique ID referenced by "portfolio_name" followed by the cryptocurrency ticker and the held amount.
            ! - Additional CryptoCurrencies can be added by putting a comma after the last Crypto ticker and amount like so:,[Crypto_Ticker]=[Amount_with_Decimal]
            ^ For example: save myportfolio1 BTC=3.3458,ETH=23.89347
                ^ This creates or overwrites a portfolio identified by the unique ID “myportfolio1”, comprised of 3.3458 Bitcoin (BTC) and 23.89347 Ethereum (ETH)."""

showArg = """show [portfolio_name] [Currency_to_Display_Holdings_in]
         ^ - The "show" argument along with the currency to display the holdings in, displays the cryptocurrencies in a portfolios holdings and their approximate value in the requested currency,
             along with the approximate valuatioon of the whole portfolio.
            ^ For example: show myportfolio1 AUD
                ^ This shows a valuation of a portfolio with the name/id of "myportfolio1" and each crypto holding in the currency of "AUD"""

# Functions
def argError():
    print(f"Error: Incomplete or invalid arguments\nUsage:\n{saveArg}\n\n{showArg}")

def checkArguments(): # https://www.cyberciti.biz/faq/python-command-line-arguments-argv-example/
    # Return Message if too many arguments are passed
    if len(sys.argv) > 4: 
        print("Too many arguments")
        return None
    elif len(sys.argv) < 4:
        argError()
        return None

    argsList = str(sys.argv) # Get the arguments list 

    return argsList

def parseCryptoArgs(cryptoArgs):
    cryptoDict = dict()
    # Split different cryptocurrencies within an argument
    cryptoHoldingList = str(cryptoArgs).split(",")
    for pair in cryptoHoldingList: # Parse pairs into the ticker and float amount, converting the ticker into uppercase and holding amount in to a float.
        try:
            ticker, holding = pair.split("=")[0].upper(), float(pair.split("=")[1])
        except: # If the holding "amount" in the argument cannot be converted to a float then the following exception will occur:
            print(f'''!!! Error, invalid arguments supplied for crypto holdings in the following pair: {pair}
            Please Ensure the Ticker is alhpabetic and the holding amount is a number that contains a maximum of one decimal point.
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\nHow to use "save":\n''', saveArg)
            return
        
        cryptoDict[ticker] = holding # Add the argument pair to a dictionary

    return cryptoDict


# Write Dict as JSON in file
def writeDictToJSONFile(directory, filename, dictionary):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(f"{directory}/{filename}.json", "w+") as outfile:
        outfile.write(json.dumps(dictionary, indent = 4))

def save(portfolioName, cryptoArgs):
    cryptoDict = parseCryptoArgs(cryptoArgs)
    writeDictToJSONFile("Portfolios", portfolioName, cryptoDict)
    print(f'Created a portfolio with the name of "{portfolioName}"" that has the following holdings: {cryptoDict}')
    return

def showPortfolioList(portfolioList):
    if len(portfolioList) == 0:
        print("There are zero portfolios stored/saved.")
    else:
        for portfolio in portfolioList:
            print(f"The amount of portfolios stored: {len(portfolioList)}")
            print(f'    - {portfolio.split(".")[0]}')

def show(portfolioName, inCurrency):
    portfolioList = os.listdir('Portfolios')
    if portfolioName not in portfolioList:
        print("!!! Error: Portfolio Name/ID is invalid, please check your input.\nPortfolio info:")
        showPortfolioList(portfolioList) # Print Portfolio IDs stored
    pass

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