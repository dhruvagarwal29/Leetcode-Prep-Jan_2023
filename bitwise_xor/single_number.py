# find the number that appears only once 

# def find_single_number(arr):
#     # one solution is using hashmap
#     hashmap = {}
#     for i in arr:
#         hashmap[i]=hashmap.get(i, 0) + 1
#     print(hashmap)
#     for key, value in hashmap.items():
#         if value==1:
#             return key

# another solution is to implement XOR in it
# we know that XOR gave the same number back if we xor it we 0
# also if same numbers xor each other then it gives 0

def find_single_number(arr):
    num = 0
    for i in arr:
        num = num ^ i
    return num


if __name__=="__main__":
    arr= [1,4,2,1,3,2,3]
    print(find_single_number(arr))