from tickerparse import tickerparse
from stockgetter import netfonds_price
#from models import *
start = time.time()
for pair in tickerparse():
	print pair[1]
	ticker = pair[1]+".OSE"
	print netfonds_price(ticker)