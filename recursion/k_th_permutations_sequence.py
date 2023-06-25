# 60 permutaitons sequence 
# given n and k, give the kth sequence

# brute force is recursion so O(n!)

def find_permutations(arr, result, current):

    # base case

    if not arr:
        result.append(list(current))
        return

    for i in range( len(arr)):
        current.append(arr[i])
        find_permutations(arr[:i]+ arr[i+1:],result, current)
        current.pop()
    return result


if __name__=="__main__":
    arr = "123"
    result=[]
    current_list = []
    print(find_permutations(arr, result, current_list))