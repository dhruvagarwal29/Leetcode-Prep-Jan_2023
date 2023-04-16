# give all the permutations of the array

# first approach
# The time complexity of this program is O(n * n!) and space as well, this is exceptable 
# but we can decrease space complexity by using swaping in this.

def permutations(arr, result, current):

    # base case if array finishes then add the current to the result
    if not arr:
        result.append(list(current))

    for i in range(len(arr)):
        current.append(arr[i]) # append the value to current
        permutations(arr[:i]+arr[i+1:], result, current) # call recursion except the element which is 
        # added up in the current
        current.pop()

    return result


def permutations_swaping(arr, result, index):
    # space is O(n) solution 
    if index == len(arr):
        result.append(list(arr))

    for i in range(index, len(arr)):
        # swap the arr 
        arr[index], arr[i] = arr[i], arr[index] 
        permutations_swaping(arr, result, index+1)
        # swap again back so that we can move it forward for next calls
        arr[index], arr[i] = arr[i], arr[index] 

    return result

if __name__=="__main__":
    arr= [1,2,3]
    # print(permutations(arr, [], []))
    print(permutations_swaping(arr, [], 0))