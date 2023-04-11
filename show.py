#####################################
# Crypto Portfolio Tracker          #
# Enoch Kuskoff -> ZeroSource.io    #
# 11/04/2023                        #
#####################################

# Show Module

    # Imports
import os, json
from dotenv import load_dotenv
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

    #Variables
line = "════════════════════════════════════════════════════════════════════════════"

with open("./currencySymbolList.txt", "r") as currencyCode:
    currencyCodeList = currencyCode.read().split("\n") # Load Currency Codes into a list

# Load environment variables
load_dotenv()
_COINMARKETCAP_APIKEY = os.getenv('_COINMARKETCAP_APIKEY')

    # Methods

# API Request handling
def reqCMC(Amount, Crypto, inCurrency): # https://coinmarketcap.com/api/documentation/v1/#operation/getV2ToolsPriceconversion
    session = Session() # Instantiate session object
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

# Read file and Return JSON as Dict
def readJSONtoDict(directory, filename):
    with open(f"{directory}/{filename}.json", "rb") as data_file:
        return json.load(data_file)

# Display any existing portfolios as a list or print a message
def showPortfolioList(portfolioList):
    if len(portfolioList) == 0:
        print("There are zero portfolios stored/saved.")
    else:
        print(f"The amount of portfolios stored: {len(portfolioList)}")
        for portfolio in portfolioList:
            print(f'    -> {portfolio.split(".")[0]}')

# Check portfolio exists, validate currency argument, call api functioon, calculate portfolio holdings
def show(portfolioName, inCurrency):
    try:
        portfolioList = os.listdir('Portfolios')
    except:
        print("Not portfolios have been created, create one first before attempting to show one.")
    priceDict = dict()

    if (f"{portfolioName}.json") not in portfolioList: # Check if portfolio name exists on disk
        print("!!! Error: Portfolio Name/ID is invalid, please check your input.\nPortfolio info:")
        showPortfolioList(portfolioList) # Print Portfolio IDs stored
        return
    else:
        print(f"\n{line}\nDisplaying Portfolio: {portfolioName} in the Currency of: {inCurrency}\n{line}")
    
    if inCurrency.upper() not in currencyCodeList:
        print(f'!!! Error: {inCurrency}/{inCurrency.upper()} is not a valid currency Code, check it is spelled correctly and exists.')
        return
    currencyCode = inCurrency.upper()

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
    
    for crypto in priceDict: # Sum the value of all holdings
        print(f"{crypto} ${priceDict[crypto]}")
        totalValuation += priceDict[crypto]
    print(f'\n$ {totalValuation} {currencyCode}')
    return