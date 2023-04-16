# find the bad version in the given array and count no of calls

def first_bad_version(nums, k, num):
    
    if len(nums) == k:
        return nums

    # find the numnber closed to the given num and assign it to left 

    