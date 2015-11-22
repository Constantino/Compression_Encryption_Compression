from BWT import BWT

x = BWT()
string = "^BANANA@"
bwt = x.get_BWT(string)
original_string = x.invert_BWT(bwt)

print string
print bwt
print original_string



