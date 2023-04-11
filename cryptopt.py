#####################################
# Crypto Portfolio Tracker          #
# Enoch Kuskoff -> ZeroSource.io    #
# 11/04/2023                        #
#####################################

# Imports
import sys

# Functions
def argError():
    print("""Error: Incomplete or invalid arguments\nUsage:
        save [portfolio_name] [Crypto_Ticker]=[Amount_with_Decimal]
         ^ - The "save" argument creates or overwites an existing portfolio identified by the unique ID referenced by "portfolio_name" followed by the cryptocurrency ticker and the held amount.
            ! - Additional CryptoCurrencies can be added by putting a comma after the last Crypto ticker and amount like so:,[Crypto_Ticker]=[Amount_with_Decimal]
            ^ For example: save myportfolio1 BTC=3.3458,ETH=23.89347
                ^ This creates or overwrites a portfolio identified by the unique ID “myportfolio1”, comprised of 3.3458 Bitcoin (BTC) and 23.89347 Ethereum (ETH).

        show [portfolio_name] [Currency_to_Display_Holdings_in]
         ^ - The "show" argument along with the currency to display the holdings in, displays the cryptocurrencies in a portfolios holdings and their approximate value in the requested currency,
             along with the approximate valuatioon of the whole portfolio.
            ^ For example: show myportfolio1 AUD
                ^ This shows a valuation of a portfolio with the name/id of "myportfolio1" and each crypto holding in the currency of "AUD"
        """)

def checkArguments(): # https://www.cyberciti.biz/faq/python-command-line-arguments-argv-example/
    # Return Message if too many arguments are passed
    if len(sys.argv) > 4: 
        print("Too many arguments")
        return None
    elif len(sys.argv) < 2:
        argError()
        return None

    argsList = str(sys.argv) # Get the arguments list 

    return argsList

def save(portfolioName, cryptoDict):
    pass

def showPortfolioList():
    pass

def show(portfolioName, inCurrency):
    pass

# Main Instance of Program
if __name__=="__main__":
    argument = checkArguments()
    if argument is not None:
        print(argument)
    else:
        exit()
    
