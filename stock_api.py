import yfinance as yf
print("yFinance version:", yf.__version__)
import json
import random

def get_stocks():
    # load json file with snp500 data
    with open('snp500.json', 'r') as file:
        snp500 = json.load(file)

    # store symbols
    SYMBOL = random.choice(snp500)['Symbol']
    SYMBOL_2 = random.choice(snp500)['Symbol']

    # get data
    dat = yf.Ticker(SYMBOL)
    dat2 = yf.Ticker(SYMBOL_2)

    # store info
    info = dat.info
    info2 = dat2.info

    # print symbols picked
    print(f"Left Stock: {SYMBOL} \nRight Stock: {SYMBOL_2}")

    # get last updated price
    current_price = round(dat.history(period="1d")["Close"].iloc[-1], 4)
    current_price2 = round(dat2.history(period="1d")["Close"].iloc[-1], 4)

    # print info
    print("\n")
    print(f"Symbol: {SYMBOL}, "
          f"\nCurrent Price: {current_price}, "
          f"\nIndustry: {info['industry']}, "
          f"\nWebsite: {info['website']}, "
          f"\nShort Name: {info['shortName']}")
    print("\n")
    print(f"Symbol: {SYMBOL_2}, "
          f"\nCurrent Price: {current_price2}, "
          f"\nIndustry: {info2['industry']}, "
          f"\nWebsite: {info2['website']},"
          f" \nShort Name: {info2['shortName']}")

    return (
            [SYMBOL, info['shortName'], current_price, info['industry']],
            [SYMBOL_2, info2['shortName'], current_price2, info2['industry']]
            )
