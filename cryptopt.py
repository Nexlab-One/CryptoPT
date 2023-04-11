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
         ^ - The "show" argument by itself displayes a list of saved portfolios, when addition arguments are supplied, 
             such as the portfolio name along with the currency to display the holdings in,
             the approximate valuatioon of the portfolio is displayed.
            ^ For example: show myportfolio1 AUD
                ^ This shows a portfolio valuation with the name/id of "myportfolio1" in the currency of "AUD"
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

def show(portfolioName, inCurrency):
    pass

# Main Instance of Program
if __name__=="__main__":
    argument = checkArguments()
    if argument is not None:
        print(argument)
    else:
        exit()
    
