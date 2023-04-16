# Given a string, sort it based on the decreasing frequency of its characters.

# this question is like the previous one only just count the character frequencies and 
# using maxheap to sort

import heapq 
from collections import defaultdict

def frequency_sort(array):

    dict = defaultdict(int)
    for item in array:
        dict[item]+=1
    
    # traverse this  and put in the max heap
    maxHeap = [] 

    for character, frequency in dict.items():
        heapq.heappush(maxHeap, (-frequency, character))

    # printed the sorted string with multiplying with frequency 
    sorted_string = []
    while maxHeap:
        frequency , character = heapq.heappop(maxHeap)
        sorted_string.append(character*(-frequency))
    return "".join(sorted_string)
    


if __name__ == "__main__":
    Input = "Programming"
    
    result = frequency_sort(Input)

    print(result)