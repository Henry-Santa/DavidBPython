def get_price(symbol):
    import requests

    apikey = 'alphavantage'

    url = ( 'https://www.alphavantage.co/query?'
            'function=TIME_SERIES_INTRADAY'
           f'&symbol={symbol}&interval=1min&apikey={apikey}'
            '&datatype=csv')

    response = requests.get(url)
    text = response.text

    try:
        quote = text.splitlines()[1].split(',')[4]
    except IndexError:
        if 'demo purposes' in text:
            exit('\n*** NOTE ***  This demo URL can only be '
                 'used with MSFT.  To obtain live data on '
                 'other symbols, you must edit your program '
                 'to change "apikey = " variable in this '
                 'function to a user key you can obtain from '
                 'the "alphavantage" service by signing up for '
                 'a free account.  See error message below: '
                 ' \n\n' + text)

        exit('error parsing response.  Response:  ' + text)

    return quote

aa = input('please input the stock symbol you would '
               'like to buy:  ')

bb = input('please input the cash you have to invest:  ')

cc = get_price(aa)      # returns a string price

## your code goes here - calculate the # of shares
## that can be bought with the user's cash

quote = float(cc) # float, ??
wallet = float(bb) # float, ??
total_possible = round(wallet / quote) # int, ??

print("with $" + bb + " you can buy " + str(total_possible) + " shares of " + aa + " at $" + str(round(quote, 2)) + "/share")