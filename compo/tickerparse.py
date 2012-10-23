def tickerparse():
	file = open('stocklist.txt','r')
	lines = file.readlines()
	ticker_name_pair =[]
	for line in lines:
		ticker_data = []
		tickerdata = line.split('\t')
		ticker_name = str(tickerdata[0])
		ticker_data.append(ticker_name)
		ticker_data.append(tickerdata[1])
		ticker_name_pair.append(ticker_data)
	return ticker_name_pair