# given a string, sort it based on the decreasing frequency of its characters 
from heapq import *
def frequency_sort(str):
    # first make the hashmap of the frequencies of string

    frequency_map = {}
    #making the frequency map of the string one way 
    for i in str:
        if i in frequency_map:
            frequency_map[i]+=1
        else:
            frequency_map[i]=1
    print(frequency_map)

    # another way of frequency map
    # frequency_map1={}
    # for char in str:
    #     frequency_map1[char] = frequency_map1.get(char, 0) + 1
    # print(frequency_map1)


    # no we need max heap to put these in decreasing order based on frequency 

    maxheap = []

    for char, freq in frequency_map.items():
        heappush(maxheap, (-freq, char))
    print(maxheap) 

    #print thr sorted string
    # stri = ""
    # for freq, char in maxheap:
    #     char=char*(-freq)
    #     stri+=char
    # print(stri)
    ''' here we cant use above method as we have to sort the string in decreasing order also 
    not only based on the frequency so we have to pop the characters out from the heap so it again 
    can heapify the remaining characters in it and we can arrange the string accoringly'''
    
    new_sorted_string = []
    while maxheap:
        frequency, char = heappop(maxheap)
        #print(maxheap)
        for _ in range(-frequency):
            new_sorted_string.append(char)
    
    print(''.join(new_sorted_string))


if __name__=="__main__":
    str= "Programming"
    frequency_sort(str)