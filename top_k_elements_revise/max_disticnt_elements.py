# given an array of numbers and a number 'K', we need to remove 'k' numbers from array
# such that we are left with max distinct numbers

'''
1) need to find frequencies of all the numbers
2) push all numbers that are not distinct in min heap based on frequency, same time count no of all 
distinct numbers
3) follow greedy approach, in stepwise fashion, we will remove the least frequent number from heap
(i.e top element of min heap) and try to make it disticnt. we will see if we can remove all the 
occurrences of a number except one. If we can, we will increment our running count of distinct numbers. 
We have to keep a count of how many removals we have done. 

4) if removing elements from heap, we are still left with some deletions, we have to remove some 
distinct elements.

'''
from heapq import *
def max_distinct_elements(arr, k):

    distinctElementsCount = 0
    #base case
    if len(arr) <= k:
        return distinctElementsCount

    # find frequency of numbers 
    frequencyMap = {}

    for num in arr:
        if num in frequencyMap:
            frequencyMap[num]+=1
        else:
            frequencyMap[num] = 1
    

    minHeap = []
    #insert the elements whose frequency is greater than 1 into min heap 

    for num, frequency in frequencyMap.items():
        if frequency ==1:
            distinctElementsCount +=1
        else:
            heappush(minHeap, (frequency, num))
    
    # following a greedy approach, try removing least frequency numbers first from min-heap

    while k>0 and minHeap:

        frequency, num = heappop(minHeap)

        # to make element distinct, we need to remove all of its occurrences except one

        k -= frequency - 1
        if k>=0:
            distinctElementsCount+=1
    
    # if k>0, this means we have to remove some distinct elements
    if k > 0 :
        distinctElementsCount -= k

    return distinctElementsCount

if __name__=="__main__":
    arr = [7,3,5,8,5,3,3]
    k=2
    print(max_distinct_elements(arr, k))