def rotate(string):

	rotations = []

	len_string = len(string)
	new_string = string
	rotations.append(string)
	for i in range(len_string-1,0,-1):
		new_string = new_string[len_string-1]+new_string[:len_string-1]
		rotations.append(new_string)

	rotations.sort()

	return rotations

def return_BWT(rotations):

	new_string = ""

	for e in rotations:
		new_string += e[-1]

	return new_string

def invert_BWT(string):
	string_list = [e for e in string]
	sorted_list = sorted(string_list)
	len_sorted_list = len(sorted_list)
	
	for j in range(len_sorted_list-1):
		temp = []
		for i in range(len(sorted_list)):
			temp.append(string_list[i]+sorted_list[i])

		sorted_list = sorted(temp)
	
	return sorted_list[-1]

rotations = rotate("^BANANA@")
#print rotations
bwt = return_BWT(rotations)
print bwt
print invert_BWT(bwt)


