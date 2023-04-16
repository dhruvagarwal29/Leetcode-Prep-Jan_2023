# given a string, find all of ots permutations the character sequence but changinf case

def change_case(str):
    result = []

    result.append(str)

    for i in range(len(str)):
        char = str[i]
        if char.isalpha():
            current_size = len(result)
            for j in range(current_size):
                # make a copy 
                current_word = result[j]
                new_word = current_word[0:i] + char.upper() + current_word[i+1:]
                result.append(new_word)
    
    return result

if __name__=="__main__":
    str = "ab7c"

    print(change_case(str))