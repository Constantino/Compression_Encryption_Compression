import re

def rle(string):
	rle_string = ''
	index = 0
	while index < len(string):
		counter = 1
		while index+1 < len(string) and string[index] == string[index+1]:
			counter += 1
			index += 1
		rle_string += chr(205) + str(counter) + chr(205)
		rle_string += string[index]
		index += 1
	return rle_string

def invert_rle(string):
	inv_rle = ''
	regex = chr(205) + "[0-9]+" + chr(205)
	pattern = re.compile(regex)
	for g in re.finditer(pattern, string):
		inv_rle += string[g.end()] * int(g.group().lstrip(chr(205)).rstrip(chr(205)))
	return inv_rle

