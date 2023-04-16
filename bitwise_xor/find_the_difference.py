# Given two strings, find the index of the extra character that is present in only one of the strings.

def difference(str1, str2):
    result = 0
    # initialize the variable 

    for i in range(len(str1)):
        result = result ^ ord(str1[i])
    
    
    for i in range(len(str2)):
        result = result ^ ord(str2[i])
    
    # now result has the ascii value of the extra character,
    if len(str1) > len(str2):
        return str1.index(chr(result))
    else:
        str2.index(chr(result))

if __name__=="__main__":
    str1 = "mpon"
    str2 = "mno"

    print(difference(str1, str2))