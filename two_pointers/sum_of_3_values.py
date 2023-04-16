# check the sum of 3 values from array match the target

def sum_3_values(arr,target):
    for i in range(len(arr)):
        left = i+1
        right = len(arr)-1

        while left< right:
            
            if target == arr[left]+arr[right]+arr[i]:
                return arr[left],arr[right],arr[i]
            left+=1
            right-=1
    return -1,-1,-1

if __name__ == "__main__":
    arr= [1,2,4,3,6]

    a,b,c= sum_3_values(arr,8)

    print(a,b,c)