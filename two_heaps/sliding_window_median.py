#Sliding Window Median

from heap_util import *

def find_sliding_window_result(nums, k):

    left_index = 0
    right_index = k
    result = []

    #make object of class Median of stream from file heap_util 

    heap = MedianOfAStream()

    while right_index <= len(nums):
        for element in nums[left_index:right_index]: # use slicing to traverse the elements till k size 
            heap.insert_num(element)
        print("heaps", heap.max_heap, heap.min_heap)
        print("median", heap.median())
        result.append(heap.median())# save the median here in result 

        # now here we have to remove the left index element from the window and from heaps too 
        # also after removing the number we removed we have to re balance the heaps
        element_to_removed = nums[left_index]

        if element_to_removed <= -heap.max_heap[0]:
            heap.remove_number(heap.max_heap, -element_to_removed)
        else:
            heap.remove_number(heap.min_heap, element_to_removed)
            

        # now element is removed call the balance funciton of the heaps

        heap.balance_heaps()

        # increase the index 
        left_index += 1
        right_index += 1

    return result


# def find_sliding_window_result(arr, k=2):
#     left_index = 0
#     right_index = k
#     medians = []

#     while right_index <= len(arr):
#         sub_arr = arr[left_index:right_index]
#         print("subarray", sub_arr)

#         h = MedianOfAStream()
#         for item in sub_arr:
#             h.insert_num(item)
#         print("heaps", h.max_heap, h.min_heap)
#         print("median", h.median())
#         medians.append(h.median())
#         left_index += 1 
#         right_index += 1 
#     return medians
if __name__=="__main__":

    print(find_sliding_window_result([1, 2, -1, 3, 5], k=2))
    #print(find_sliding_window_result([1, 3, -1, -3, 5, 3, 6, 7], k = 3))


    

