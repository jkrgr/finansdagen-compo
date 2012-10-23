from tickerparse import tickerparse
from stockgetter import netfonds_price
from models import *
for pair in tickerparse():
	print pair
