# 0/1 knapsack problem 

#Let's solve the 0/1 Knapsack problem using the Dynamic Programming pattern.

def knapsack(weights, values, capacity):
    for i in range(capacity+1):
        profits = [0] * i

    for index in range(len(weights)):
        for cap in range(capacity, -1 , -1):
            if weights[index] <= cap:
                profit = values[index] + profits[cap - weights[index]]
                # if profit > profits[i]:
                profits[i] = profit
                




if __name__ == "__main__":
    weights = [1,2,3,5]
    values = [10,5,4,8]
    capacity = 5

    max_profit = knapsack(weights, values, capacity)

    print(max_profit)