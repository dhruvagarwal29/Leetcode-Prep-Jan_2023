#find the cycle in array        

def circular_loop_exists(arr):
    is_Forward = False
    for element in range(len(arr)):
        if arr[element] >= 0:
            is_Forward = True # making forward step if element is positive 

            slow = element
            fast = element
            # if slow or fast becomes -1 this means we cant find cycle for this number 
            while True:
                # move one step for slow pointer
                slow = find_next_index(arr, is_Forward, slow)
                # move one step for fast pointer
                fast = find_next_index(arr, is_Forward, fast)

                if (fast != -1):
                    # move another step for fast pointer
                    fast = find_next_index(arr, is_Forward, fast)

                if slow == -1 or fast == -1 or slow == fast:
                    break

            if slow != -1 and slow==fast:
                return True 
    
    return False

def find_next_index(arr, is_Forward, current_index):
    direction = False

    if arr[current_index] >= 0:
        direction = True
    
    if is_Forward != direction:
        return -1 # change the direction, return -1

    next_index = (current_index + arr[current_index]) % len(arr)

    # one element cycle, return -1 

    if next_index == current_index:
        next_index = -1

    return next_index

if __name__ == "__main__":
    print(circular_loop_exists([1,2,-1,2,2]))
    print(circular_loop_exists([2,2,-1,2]))
    print(circular_loop_exists([2,1,-1,-2]))


