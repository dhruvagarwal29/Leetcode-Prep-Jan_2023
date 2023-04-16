from heap_util import *

def medi(arr):

    heap= MedianOfAStream()

    for element in arr:
        heap.insert_num(element)


    return heap.median()


if __name__=="__main__":
    arr = [3,1,5]
    print(medi(arr))
