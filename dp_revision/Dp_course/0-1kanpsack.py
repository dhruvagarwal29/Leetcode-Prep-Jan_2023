# 0-1 kanpsack using naive recursion, topdown(dp), bottomup (dp)
# You want to maximize the sum of values of the items in your knapsack while
# ensuring that the sum of the weights of the items remains less than or equal to 
# the knapsack’s capacity.

# naive recursion 


def naive_recursion(weights, values, capacity, current_index):
    # base case if lenght of weights is equal to current index or capacity is 0 then gives 0
    if capacity ==0 or current_index >= len(weights):
        return 0
    
    # you take the element 
    sum_profit1 = 0 #variable used to calcualte values starting from 0 element 
    
    # so if weights of current index is samller or equal then add the profits lying on current index 
    # and recusively call the fucntion with reduced capacity and current index 
    if weights[current_index] <= capacity:
        sum_profit1 = values[current_index] + \
        naive_recursion(weights, values, capacity - weights[current_index], current_index+1)
    

    # you dont take the element
    sum_profit2 = 0 #variable used to calcualte values starting from 1 element
    sum_profit2 = naive_recursion(weights, values, capacity, current_index +1)
    
    
    return max(sum_profit1, sum_profit2)





# def naive_recursion(weights, values, capacity, i):

#     if i == len(weights):
#         return 0
    
#     if capacity == 0:
#         return 0
    
#     if capacity < 0:
#         return 0

#     val1 = 0

#     # if weights[i] <= capacity:
#     #     val1 = values[i] + naive_recursion(weights, values, capacity - weights[i], i+1)
        
#     val2 = naive_recursion(weights, values, capacity, i+1)

#     return max(val1, val2)


# bottom up approach (memoization)




if __name__== "__main__":

    weights = [3, 2, 1, 5]
    values = [4, 5, 10, 8]
    capacity = 5
    current_index = 0
    print(naive_recursion(weights, values, capacity, current_index))
 