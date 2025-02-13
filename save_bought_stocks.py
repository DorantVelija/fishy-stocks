import csv
import datetime

PRICE_PER_STOCK = 10

# write csv file headers if not already there
def write_header_if_needed():
    try:
        with open('stocks_bought.csv', 'x', newline='') as csvfile:
            fieldnames = ['symbol', 'short_name', 'price_bought', 'industry', 'date', 'stock_owned']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    except FileExistsError:
        pass

# else, write data to csv file
def write_to_csv(data):
    write_header_if_needed()
    with open('stocks_bought.csv', 'a', newline='') as csvfile:
        fieldnames = ['symbol', 'short_name', 'price_bought', 'industry', 'date', 'stock_owned']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows(data)

# read data and write to csv
def read_row(symbol, short_name, price_bought, industry):
    data = [
        {'symbol': symbol,
         'short_name': short_name,
         'price_bought': price_bought,
         'industry': industry,
         'date': str(datetime.datetime.now())[:10],
         'stock_owned': PRICE_PER_STOCK/price_bought
         }
    ]
    write_to_csv(data)
