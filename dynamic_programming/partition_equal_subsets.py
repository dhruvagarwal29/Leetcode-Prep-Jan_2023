#Given a non-empty array of positive integers, 
# determine if the array can be divided into two subsets so that the sum of both the subsets is equal.


def equal_subset(array):
    
    array_sum = sum(array) # total sum

    # make a 2D matrix to solve this question

    sum_to_find = array_sum //2  # this is the sum which we have to find in dp
    dp = []
    # for j in range(sum_to_find+1):
    #     col = []
    #     for i in range(len(array)+1):
    #         col.append(False)
    #     dp.append(col)

    dp = [[False for i in range(len(array)+1)] for j in range(sum_to_find+1)] # same as above
    # print(dp)
    # print(matrix)

    # place true in first row of the matrix 
    for i in range(len(array)+1):
        
    


if __name__ =="__main__":
    array = [1,3,7,3]

    print(equal_subset(array))