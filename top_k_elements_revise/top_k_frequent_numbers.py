# given an unsorted array of #s, find the top 'k' frequently occurring numbers in it

# use hasmap to count the frequencirs and then use min heap to place those frequencies in the heap 
from heapq import *
def top_k_frequent_nos(arr, k):
    # make a hashmap of frequencies 
    frequency_map = {}
    # how to count frequency
    for num in arr:
        if num in frequency_map:
            frequency_map[num]+=1
        else:
            frequency_map[num] = 1

    # now minheap 
    minheap = [] 
    for num, freq in frequency_map.items():
        #print (num, freq)
        heappush(minheap, (freq, num))   # here we are storing the elements in heap according to frequency
        # NOT to numbers 
        if len(minheap)>k:  
            heappop(minheap)
    
    return minheap

    #print(frequency_map)
if __name__=="__main__":
    arr = [1,3,5,12,11,12,11]
    k=2
    print(top_k_frequent_nos(arr,k))