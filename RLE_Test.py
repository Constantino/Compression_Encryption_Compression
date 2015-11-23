from BWT import BWT, invert_BWT
from RLE import rle, invert_rle

string = "^BANANA@"
transformed_string = BWT(string)
original_string = invert_BWT(transformed_string)

print string
print transformed_string
print original_string

rle_string = rle(transformed_string)
print rle_string
rle_original = invert_rle(rle_string)
print rle_original