import os, os.path, json

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