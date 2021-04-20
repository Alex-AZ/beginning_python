# -*- coding: utf8 -*-
import random
import json

def read_values_from_json(path, key):
	# Create a new empty list:
	values = []
	# Open a json file with my objects:
	with open(path) as f:
		# Load all the data contained in this file
		data = json.load(f)
		# Add each item in my list:
		for entry in data:
			values.append(entry[key])
	# Return my completed list:
	return values

# Give a json and return a list
def clean_strings(sentences):
	cleaned = []
	# Store quotes on a list. Create an empty list and add each sentence on by one.
	for sentence in sentences:
		# Clean quotes from whitespace and so on
		clean_sentence = sentence.strip()
		# Don't use extend as it adds each letter on by one!
		cleaned.append(clean_sentence)
	return cleaned

# Return a random item in a list
def get_random_item_in(object_list):
	rand_numb = random.randint(0, len(object_list) - 1) # get a random number
	return object_list[rand_numb] # return the item

def random_value(source_path, key):
	all_values = read_values_from_json(source_path, key)
	clean_values = clean_strings(all_values)
	return get_random_item_in(clean_values)


######################
####### QUOTES #######
######################

# Gather quotes from San Antonio

# Return a random value from a json file
def random_quote():
	return random_value('quotes.json', 'quote')


######################
#### CHARACTERS ######
######################

# Gather (rassembler) characters from Wikipedia 

def random_character():
	return random_value('characters.json', 'character')


######################
#### INTERACTION #####
######################

# Print a random sentence.

def print_random_sentence():
	rand_quote = random_quote()
	rand_character = random_character()
	print(">>>> {} said : {}".format(rand_character, rand_quote))

def main_loop():
	while True:
		print_random_sentence()
		message = ('Would you like another true quote?'
					'Type [enter].'
					'To exit, type [B].')
		choice = input(message).upper()
		if choice == 'B':
			break
			# This will stop the loop!

if __name__ == '__main__':
	main_loop()