# Longest Substring with K Distinct Characters (medium)

# def bruteforce_subarray(arr, k):

'''
this solution is working but set are unordered data structure so we have to take a dictionary
'''
#   start = 0
#   str = []
#   str_set = {arr[0]}
#   window_size=0
#   for i in range(1,len(arr)):
#     str_set.add(arr[i])
#     if len(str_set) > k:
#         window_size = i - start
#         start +=1 
#         # print(s[])
#         str_set.pop() 
#   print(window_size)
        

def subarray(arr, k):
    start = 0
    window_size = 0
    longest_dict = {}
    # traverse through the array
    for end in range(len(arr)):
        longest_dict[arr[end]] = 1    # put any value for the added element in dictionary, I am taking 1
        # if length of dict is equal to the k then update the window size with (end +1 ) - start
        if (len(longest_dict) == k):
            window_size = ((end + 1) - start)
        print(longest_dict)
        # for more distinct characters than k in the dict then 
        if (len(longest_dict)> k):
            longest_dict.pop(arr[start])
            start +=1

    return window_size

if __name__ == "__main__":
    
    result = subarray("abcbbc",2)
    print(subarray("araaci",2))
    # print(result1)