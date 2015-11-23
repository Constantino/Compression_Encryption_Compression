import re

def rle(string):
	rle_string = ''
	index = 0
	while index < len(string):
		counter = 1
		while index+1 < len(string) and string[index] == string[index+1]:
			counter += 1
			index += 1
		rle_string += str(counter)
		rle_string += string[index]
		index += 1
	return rle_string

def invert_rle(string):
	inv_rle = ''
	pattern = re.compile("[0-9]+|\\p{ASCII}")
	for g in re.finditer(pattern, string):
		inv_rle += string[g.end()] * int(g.group())
	return inv_rle

