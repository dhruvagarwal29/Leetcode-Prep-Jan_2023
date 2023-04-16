# find all the permutations of the string 

def string_permutation(str):
    result_string = [[str[0]]]

    for i in range(1,len(str)):
        char = str[i]
        current_size = len(result_string)
        for i in range(current_size):
            new_list = result_string.pop(0)
            for j in range(len(new_list)+1):
                copy_list = new_list.copy()
                copy_list.insert(j, char)
                result_string.append(copy_list)
        
    result = ["".join(item) for item in result_string]

    return result




if __name__=="__main__":
    str = "bad"
    print(string_permutation(str))