from collections import deque
def abbre(str):
    result = deque()
    result.append("")
    for i in range(len(str)):
        char = str[i]
        current_size = len(result)
        for i in range(current_size):
            new_str = result.popleft()
            # adding the _ 
            result.append(new_str + "_")
            # ading the char
            result.append(new_str + char)

    return change_char(list(result))

def change_char(arr):
    result = []
    for word in arr:
        count = 0
        new_word = ""
        for i in range(len(word)):
            if word[i] =="_":
                count += 1
            else:
                if count > 0:
                    new_word += str(count) + word[i]
                    count = 0
                else:
                    new_word += word[i]
                    count = 0

        if count > 0:
            new_word = new_word + str(count)
        result.append(new_word)
     
    return result



        
   # return result

if __name__=="__main__":
    print(abbre("BAT"))