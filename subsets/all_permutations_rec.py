# find the permutation of string using recursion 

    
def string_permutation(str):
    answer = ""
    result = []
    string_permutation_rec(str, answer, result)
    return result

def string_permutation_rec(s, answer, result):
    if (len(s) == 0):
        result.append(answer)
      
     
 
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        #print(left_substr)
        right_substr = s[i + 1:]
        #print(right_substr)
        rest = left_substr + right_substr
        string_permutation_rec(rest, answer + ch, result)
        
        
    return result
 


if __name__=="__main__":
    str = "bad"
    print(string_permutation(str))