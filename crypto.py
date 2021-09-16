# API URLs
# Bitcoin - https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD
# Monero - https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD
# Raven - https://min-api.cryptocompare.com/data/price?fsym=RVN&tsyms=USD
# Dogecoin - https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD
# ZCash - https://min-api.cryptocompare.com/data/price?fsym=ZEC&tsyms=USD


import requests


class Price:
    '''A Class to track the price of a cryptocurrency'''

    # Variables
    global x
    global coins
    global tickers
    
    x = True
    coins = ['BITCOIN', 'ETHEREUM', 'MONERO', 'RAVEN', 'DOGECOIN', 'ZCASH', 'LITECOIN', 'XRP', 'UNISWAP', 'TRON', 'ANIMECOIN', 'GARLICOIN']
    tickers = ['BTC', 'ETH', 'XMR', 'RVN', 'DOGE', 'ZEC', 'LTC', 'XRP', 'UNI', 'TRX', 'ANI', 'GRLC']
    
    def api():
        response = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={tickers[index]}&tsyms=USD")
        data = response.json()
                
        print(f"\n\n\tPRICE OF {coins[index]} $\n\t=====================\n\t{tickers[index]}   ---   $ " + str(data["USD"]))


    def getPrice():
        global index

        while x:
            # Main Interaction
            currency = input(f"\n{coins}\n\nEnter a coin or ticker, and track its price:  ").upper()

            try:
                if currency in tickers:
                    index = tickers.index(currency)
                    Price.api()
                elif currency in coins:
                    index = coins.index(currency)
                    Price.api()


            except:
                print("\nPlease enter a valid coin...\n")
                
            null = input('\n\nPress ENTER to restart program')
            
            

Price.getPrice()