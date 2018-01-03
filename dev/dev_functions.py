import requests

#-----CRYPTOCOMPARE API
#Returns dictionary matching all coin names to their API codes
def get_name_to_coin():
	name_to_coin = {}

	#Special
	name_to_coin['us dollars'] = 'USD'

	#Fetch all coins from cryptocompare API
	coin_request = requests.get('https://min-api.cryptocompare.com/data/all/coinlist')
	request_json = coin_request.json()
	coin_data = request_json['Data']

	#Buid full name_to_coin
	for coin in coin_data:
		this_coin_data = coin_data[coin]
		name = this_coin_data['CoinName'].lower()
		code = this_coin_data['Name'].upper()
		existing = False
		for existing_name in name_to_coin:
			if existing_name.lower() == name.lower():
				existing = True
		if not existing:
			if ' /' in name:
				slash_index = name.index(' /')
				name = name[:slash_index]
			name_to_coin[name] = code

	return name_to_coin

#-----UTILITY
#Prints a given dictionary with a certain number of keys per line, ready to be pasted into a .py file
def print_dictionary(dictionary, keys_per_line):
	last_index = len(dictionary)
	print('{', end='')
	index = 1
	for key in dictionary:
		print('\'' + key + '\' : \'' + dictionary[key] + '\'', end='')
		if index != last_index:
			print(', ', end='')
			if index % keys_per_line == 0:
				print()
		index += 1
	print('}', end='')