#Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

# we are going to use hashmap to count the frequency then use minheap

import heapq 
from collections import defaultdict


def top_k_elements(array, k):

    dict = defaultdict(int)
    for item in array:
        dict[item]+=1
    
    # return dict   output -=>  {1: 1, 3: 1, 5: 1, 12: 2, 11: 2} (number:frequency)  dict is made like this now I can 
    # traverse this  and put in the min heap
    minHeap = [] 

    for number, frequency in dict.items():
        heapq.heappush(minHeap, (frequency, number))
        # this condition will allow to remove the min freq elements from the min heap
        if len(minHeap)> k:
            heapq.heappop(minHeap)

    #return minHeap
    # create list of top k numbers 
    result = []
    while minHeap:
        num = heapq.heappop(minHeap)[1] # numbers only not frequencies 
        # other way _, num = heapq.heappop(minHeap)
        result.append(num)
    return result


if __name__ == "__main__":
    Input = [1, 3, 5, 12, 11, 12, 11] 
    K = 2
    result = top_k_elements(Input,K)

    print(result)

