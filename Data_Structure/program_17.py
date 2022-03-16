# Print reverse string using recursion

raw_string = "helloworld"

length_of_rawstring = len(raw_string)
def rev_str(raw_string, length_of_rawstring):
    length_of_rawstring -= 1
    if length_of_rawstring == 0:
        return raw_string[length_of_rawstring]
    return raw_string[length_of_rawstring] + rev_str(raw_string,length_of_rawstring) 

print(rev_str(raw_string,length_of_rawstring))