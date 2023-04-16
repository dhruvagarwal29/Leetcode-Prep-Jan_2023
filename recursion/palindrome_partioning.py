# partion the string so as each partition is a palindrome
#131 leetcode

def partition_string(str, index, result, current_list):

    if index == len(str):
        result.append(list(current_list))
        return

    for i in range(index, len(str)):
        if is_palindrome(str, index, i):  # check the partition from index to i 
            current_list.append(str[index:i+1])
            partition_string(str,i+1, result, current_list)
            current_list.pop()

    return result

def is_palindrome(str, start, end):
    while start<= end:
        if str[start] != str[end]:
            return False
        start+=1
        end-=1
    return True

if __name__=="__main__":
    str = 'aabb'
    result = []
    current_list = []
    print(partition_string(str,0, result , current_list))
