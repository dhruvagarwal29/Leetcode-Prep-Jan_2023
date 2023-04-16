# Given an array of characters where each character represents a fruit tree, you are 
# given two baskets and your goal is to put maximum number of fruits in each basket. 
# The only restriction is that each basket can have only one type of fruit.

'''
This question is same as the k_longest_subarray.py
'''

def subarray(arr, k):
    start = 0
    window_size = 0
    fruit_basket = {}

    for i in range(len(arr)):
        fruit_basket[arr[i]] = 1

        if (len(fruit_basket) == k):
            window_size = (i + 1) - start
        
        if (len(fruit_basket)> k):
            fruit_basket.pop(arr[start])
            start +=1

    print(window_size)
if __name__ == "__main__":
    Fruit=['A', 'B', 'C', 'B', 'B', 'C']
    k=2 
    result = subarray(Fruit,k)