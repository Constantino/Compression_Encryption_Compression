from BWT import BWT, invert_BWT

string = "^BANANA@"
transformed_string = BWT(string)
original_string = invert_BWT(transformed_string)

print string
print transformed_string
print original_string



