# PolyStock
Display stock prices on polybar...

## Dependencies

### Python Modules
* `yahoo_fin`
* `argparse`

## Module
```ini
[module/polystock]
type = custom/script
;Options for output:
;--biggestloser: Prints the stock with the biggest drop in a given day.
;--biggestgainer: Prints the stock with the biggest gain in a given day.
;--mostactive: Prints the most active stock in a given day.
;--topcrypto: Prints the top cryptocurrency by market cap in a given day.
;--customticker: Takes a stock ticker (ex. AAPL, GOOGL, VZ) and outputs the live price of that stock.
exec = ~/polybar-scripts/polystock.py --
# For continuous updates:
tail = true
label = %output%
```


