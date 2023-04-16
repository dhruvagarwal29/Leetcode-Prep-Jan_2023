# Given two integer arrays, gas and cost, return the starting gas station’s index if 
# we can travel around the circuit once in the clockwise direction. Otherwise, return −1


# If there exists a solution, it is guaranteed to be unique.


def starting_index(gas, cost):
    start_index = 0
    gas = 0

    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
    if total_gas != total_cost: return -1


    for i in range(len(gas)):
        gas += cost[i] - gas[i]

        if gas < 0:
            gas = 0
            

if __name__ == "__main__":

    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    starting_ind = starting_index(gas, cost)

    print(starting_ind)