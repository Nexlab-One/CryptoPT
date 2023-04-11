#####################################
# Crypto Portfolio Tracker          #
# Enoch Kuskoff -> ZeroSource.io    #
# 11/04/2023                        #
#####################################

# Imports
import os, os.path, sys, json
from dotenv import load_dotenv
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# Load environment variables
load_dotenv()
_COINMARKETCAP_APIKEY = os.getenv('_COINMARKETCAP_APIKEY')

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

line = "════════════════════════════════════════════════════════════════════════════"
# Methods

    # Requests
def reqCMC(Amount, Crypto, inCurrency): # https://coinmarketcap.com/api/documentation/v1/#operation/getV2ToolsPriceconversion
    url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': _COINMARKETCAP_APIKEY,
    }
    session.headers.update(headers)
    body = {
        'amount': Amount,
        'symbol': Crypto,
        'convert': inCurrency
    }
    
    try:
        response = session.get(url, params=body)
        data = json.loads(response.text)
        return True, data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return False, e

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

# Read file and Return JSON as Dict
def readJSONtoDict(directory, filename):
    with open(f"{directory}/{filename}.json", "rb") as data_file:
        return json.load(data_file)

def save(portfolioName, cryptoArgs):
    cryptoDict = parseCryptoArgs(cryptoArgs)
    writeDictToJSONFile("Portfolios", portfolioName, cryptoDict)
    print(f'Created a portfolio with the name of "{portfolioName}"" that has the following holdings: {cryptoDict}')
    return

def showPortfolioList(portfolioList):
    if len(portfolioList) == 0:
        print("There are zero portfolios stored/saved.")
    else:
        print(f"The amount of portfolios stored: {len(portfolioList)}")
        for portfolio in portfolioList:
            print(f'    -> {portfolio.split(".")[0]}')

def show(portfolioName, inCurrency):
    portfolioList = os.listdir('Portfolios')
    if (f"{portfolioName}.json") not in portfolioList:
        print("!!! Error: Portfolio Name/ID is invalid, please check your input.\nPortfolio info:")
        showPortfolioList(portfolioList) # Print Portfolio IDs stored
        return
    else:
        print(f"\n{line}\nDisplaying Portfolio: {portfolioName} in the Currencey of: {inCurrency}\n{line}")
    
    if inCurrency.upper() not in currencyCodeList:
        print(f'!!! Error: {inCurrency}/{inCurrency.upper()} is not a valid currency Code, check it is spelled correctly and exists.')
        return
    currencyCode = inCurrency.upper()

    priceDict = dict()
    # Read Portfolio
    portfolioDict = readJSONtoDict("Portfolios", portfolioName)
    for crypto in portfolioDict:
        cryptoTicker = crypto
        amount = portfolioDict[crypto]
        success, cmcResponse = reqCMC(amount, cryptoTicker, currencyCode) # Fetch Data from API
        if success:
            priceDict[crypto] = cmcResponse['data'][0]['quote'][currencyCode]['price'] # Extract price from Data
        else:
            print("Error Processing Request, see following error response for more information:\n",cmcResponse)
            return
    totalValuation = 0.00
    for crypto in priceDict:
        print(f"{crypto} ${priceDict[crypto]}")
        totalValuation += priceDict[crypto]
    print(f'\n$ {totalValuation} {currencyCode}')
    return

# Main Instance of Program
if __name__=="__main__":
    session = Session() # Instantiate session object
    argument = checkArguments() # Check to ensure that valid and correct amount of arguments were supplied.

    with open("currencySymbolList.txt", "r") as currencyCode:
        currencyCodeList = currencyCode.read().split("\n") # Load Currency Codes into a list
    
    if argument is not None:
        match sys.argv[1]: # Match first argument to relevant method and call it.
            case "save":
                save(sys.argv[2], sys.argv[3]) # Pass following arguments to save method.
            case "show":
                show(sys.argv[2], sys.argv[3]) # Pass following arguments to save method.
    else:
        exit()