#Run this to generate Amazon Developer information
#It will produce three text files in the output directory: 'intent_schema.txt', 'custom_slot_COIN.txt', and 'sample_utterances.txt'.
#These can be pasted into the analogous Amazon Developer Console sections

import os
from function_package_files import coincheck_data

#Determine relevant paths
root_path = os.path.dirname(os.path.realpath(__file__))
output_path = root_path + '\\output'

#Slot names
source_coin_slot_name = 'SourceCoin'
target_coin_slot_name = 'TargetCoin'
#Intent names
check_price_intent_name = 'CheckPrice'

#Prints the intent schema
def print_intent_schema():
	filename = 'intent_schema.txt'
	print('Writing to', filename, '...')
	intent_schema_file = open(output_path + '\\' + filename, 'w')
	intent_schema_file.write('{\n')
	intent_schema_file.write('	"intents": [\n')
	intent_schema_file.write('		{\n')
	intent_schema_file.write('			"slots": [\n')
	intent_schema_file.write('				{\n')
	intent_schema_file.write('					"name": "' + source_coin_slot_name + '",\n')
	intent_schema_file.write('					"type": "COINS"\n')
	intent_schema_file.write('				},\n')
	intent_schema_file.write('				{\n')
	intent_schema_file.write('					"name": "' + target_coin_slot_name + '",\n')
	intent_schema_file.write('					"type": "COINS"\n')
	intent_schema_file.write('				}\n')
	intent_schema_file.write('			],\n')
	intent_schema_file.write('			"intent": "' + check_price_intent_name + '"\n')
	intent_schema_file.write('		}\n')
	intent_schema_file.write('	]\n')
	intent_schema_file.write('}\n')
	intent_schema_file.close()
	print('SUCCESS!')

#Prints the coin name list for the Coin slot type
def print_coin_slot_list():
	filename = 'custom_slot_COIN.txt'
	print('Writing to', filename, '...')
	coin_slot_file = open(output_path + '\\' + filename, 'w', encoding='utf-8')
	for name in coincheck_data.name_to_code:
		coin_slot_file.write(name + '\n')
	coin_slot_file.close()
	print('SUCCESS!')

#Prints the list of sample utterances, pretty trivial
def print_sample_utterances():
	filename = 'sample_utterances.txt'
	print('Writing to', filename, '...')
	sample_utterances_file = open(output_path + '\\' + filename, 'w')
	#Check price intent
	for utterance in 	[
						'What is the price for {{{}}}'.format(source_coin_slot_name),
						'What is the price for {{{}}} in {{{}}}'.format(source_coin_slot_name, target_coin_slot_name),
						'What\'s the price for {{{}}}'.format(source_coin_slot_name),
						'What\'s the price for {{{}}} in {{{}}}'.format(source_coin_slot_name, target_coin_slot_name),
						'Check the price for {{{}}}'.format(source_coin_slot_name),
						'Check the price for {{{}}} in {{{}}}'.format(source_coin_slot_name, target_coin_slot_name)
						]:
		sample_utterances_file.write(check_price_intent_name + ' ' + utterance + '\n')
	sample_utterances_file.close()
	print('SUCCESS!')

#Create output directory
if not os.path.exists(output_path):
	print('Making /output/ directory ...')
	os.makedirs(output_path)
	print('SUCCESS!')

print_intent_schema()
print_coin_slot_list()
print_sample_utterances()

print('Done.')