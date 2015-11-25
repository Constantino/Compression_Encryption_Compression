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

def get_BWT(string):

    rotations = rotate(string)
    new_string = ""

    for e in rotations:
        new_string += e[-1]

    return new_string

def BWT(string):
    
    assert "\0" not in string, "Input string cannot contain null character ('\\0')"
    string += "\0"  # Add end of file marker

    return get_BWT(string)


def invert_BWT(r):
    
    table = [""] * len(r)  
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  
    s = [row for row in table if row.endswith("\0")][0]  
    return s.rstrip("\0")  


