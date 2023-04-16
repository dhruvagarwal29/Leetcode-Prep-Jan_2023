# find the missing number 

def missing_number(arr):

    start = 0

    while start < len(arr):

        pointer_to_compare = arr[start]
        # print ("start",arr[start], arr[pointer_to_compare-1])
        if  arr[start] < len(arr) and arr[start] != arr[pointer_to_compare]:
            print (arr[start], arr[pointer_to_compare])
            arr[start], arr[pointer_to_compare] = arr[pointer_to_compare], arr[start]
        else:
            start +=1 
        
    i = 0
    while True:
        if i != arr[i]:
            return i
        else:
            i+=1

    

if __name__=="__main__":
    arr= [4,0,1,50]
    print(missing_number(arr))