#!/usr/bin/env python3

"""
Polystock
Author: Zachary Ashen
Date: May 9th 2020
Description: A ticker displayer for polybar.
Displays the days highest gainer, biggest loser,
top crypto or any custom stock ticker.
Contact: zachary.h.a@gmail.com
"""

from yahoo_fin import stock_info as si
import argparse

# How many decimal place to show in stock price.
roundNumber = 1

def biggestloser():
    """Returns: stock with the the biggest losses in a given day and
    its stock price with format: 'TICKER': 'PRICE'."""

    day_losers = si.get_day_losers()
    output = str(day_losers.at[0, 'Symbol']) + ': ' + str(round(si.get_live_price(day_losers.at[0, 'Symbol']), roundNumber))
    return output

def biggestgainer():
    """Returns: stock with the biggest gains in a given day and
    its stock price with format: 'TICKER': 'PRICE'."""

    day_gainer = si.get_day_gainers()
    output = str(day_gainer.at[0, 'Symbol']) + ': ' + str(round(si.get_live_price(day_gainer.at[0, 'Symbol']), roundNumber))
    return output

def mostactive():
    """Returns: stock with the most activity in a given day and
    its stock price with format: 'TICKER': 'PRICE'."""

    day_active = si.get_day_most_active()
    output = str(day_active.at[0, 'Symbol']) + ': ' + str(round(si.get_live_price(day_active.at[0, 'Symbol']), roundNumber))
    return output

def customticker(tickers):
    """Returns: stock price and ticker of a stock with format 'TICKER': 'PRICE'.
    Parameter: the ticker to get a stock price on and to display.
    Precondition: ticker is a string[]."""

    output = []
    for ticker in tickers:
        tickerPrice = si.get_live_price(ticker)
        output.append(ticker + ': ' + str(round(tickerPrice, roundNumber)))

    return ' '.join(output)

def topcrypto():
    """Returns: cryptocurrency with the highest price in a given day and its name
    with format: 'CRYPTO': 'PRICE'."""

    top_crypto = si.get_top_crypto()
    output = str(top_crypto.at[0, 'Symbol']) + ': ' + str(round(si.get_live_price(top_crypto.at[0, 'Symbol']), roundNumber))
    return output

def addArguments():
    """Adds arguments from ArgParse and parses them to handle arguments"""

    parser = argparse.ArgumentParser(description='Displays stock prices outputted in a simplified form for polybar.', epilog='Output will always be in the format of: Biggest Loser, Biggest Gainer, Most Active, Top Crypto, Custom Ticker')

    # add arguments to be called
    parser.add_argument('--biggestloser', help='Prints the stock with the biggest drop in a given day.', action='store_true')
    parser.add_argument('--biggestgainer', help='Prints the stock with the biggest gain in a given day.', action='store_true')
    parser.add_argument('--mostactive', help='Prints the most active stock in a given day.', action='store_true')
    parser.add_argument('--topcrypto', help='Prints the top cryptocurrency by market cap in a given day.', action='store_true')
    parser.add_argument('--customticker', action='append', help='Display the price of a custom ticker.', type=str)

    args = parser.parse_args()

    stocks = []

    # parse arguments
    if args.biggestloser:
        stocks.append(biggestloser())
    if args.biggestgainer:
        stocks.append(biggestgainer())
    if args.mostactive:
        stocks.append(mostactive())
    if args.topcrypto:
        stocks.append(topcrypto())
    if args.customticker:
        stocks.append(customticker(args.customticker))


    if len(stocks) == 0:
        print("You must choose a stock to be displayed! Use --help for more details...")
    else:
        print(stocks)

if __name__ == '__main__':
    addArguments()
