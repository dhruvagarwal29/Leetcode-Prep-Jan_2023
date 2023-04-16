# find the two single number from the array of duplicates 
#first method
# def two_single_number(arr):
#     # first find the xor of both the numbers

#     n1_xor_n2 = 0
#     for i in arr:
#         n1_xor_n2 = n1_xor_n2 ^ i 

#     #print(n1_xor_n2)

#     # now we have to seperate the n1 and n2 from n1xorn2

#     # for that we c 
#     # the least significant bit can be found with number ^ (-number)

#     bitwise_mask = n1_xor_n2 & (-n1_xor_n2) 
#     # divide into two groups of numbers, here we want the group with bit set
#     # which results in one of the numbers we want due to the property X ^ X = 0
#     result = 0
#     for i in arr:
#         if bitwise_mask & i :
#             result = result ^ i

#     return [result, result ^ n1_xor_n2]

def two_single_number(arr):
    n1_xor_n2 = 0
    for i in arr:
        n1_xor_n2 = n1_xor_n2 ^ i

    n1, n2 = 0,0
    # get the rightmost bit that is "1"
    right_most_bit = 1
    while(right_most_bit & n1_xor_n2) == 0:
        right_most_bit = right_most_bit << 1

    n1, n2 = 0,0
    for num in arr:
        if(num & right_most_bit): # the bit is set
            n1 = n1 ^ num
        else: # the bit is not set
            n2 = n2 ^ num 
    
    return [n1, n2]


if __name__=="__main__":
    arr = [4, 4, 3, 2, 3, 5]
    print(two_single_number(arr))