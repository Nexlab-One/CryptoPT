#####################################
# Crypto Portfolio Tracker          #
# Enoch Kuskoff -> ZeroSource.io    #
# 11/04/2023                        #
#####################################

# Args Module

    # Imports
import sys

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
                ^ This shows a valuation of a portfolio with the name/id of "myportfolio1" and each crypto holding in the currency of "AUD
                
        ^ - An API Key for showing the value of a portfolio using CoinMarketCaps' API is required. Add it to the .env file if running locally, or in the dockerfile before composing."""

    # Methods

# Error message to display when arguments are invalid
def argError():
    print(f"Error: Incomplete or invalid arguments\nUsage:\n{saveArg}\n\n{showArg}")

# Basic argument check and parse
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