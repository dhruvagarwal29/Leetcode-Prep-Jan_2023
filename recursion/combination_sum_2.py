# leetcode 40 question 

# give the sequences whose sum is equal to target but here repeatation of elements is not allowed 
# also there should be not repeated patterns 

# THIS IS ANOTHER PATTERN TO SOLVE RECURSION WITH ARRAY
def combination_sum(arr, target, index, result, current):
    # base case 
    if target == 0:
        result.append(list(current))
        return
    # now elements can not repeated so to take that into consideration in "take element" part 
    # we are going to loop to increase the index over here in recursion call 

    for i in range(index, len(arr)):
        if arr[i] > target:
            break # break the loop if arr value is greater then target 

        # now if condition if previous element is equal to the currrent element
        # one more condition is that to if 1st index is picked and that
        #  is same by 2nd index so not pick it again but only if current index is greater than index
        # otherwise u will never pick the duplicate element and that will lose some sequences
        if i > index and arr[i] == arr[i-1]:
            continue
        current.append(arr[i])
        combination_sum(arr, target - arr[i], i+1, result, current) # decrease the target 
        current.pop()

    


if __name__=="__main__":

    arr= [10,1,2,7,6,1,5]
    # SORT THE ARRAY SO THAT ELEMENTS WILL BE SORTED 
    arr.sort()
    target = 8
    result = []
    combination_sum(arr, target, 0, result, [])
    print(result)