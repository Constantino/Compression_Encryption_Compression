def BWT(string):
    table = [string[n:] + string[:n] for n in xrange(len(string))]
    table = sorted(table)
    return "".join([rotation[-1] for rotation in table])

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