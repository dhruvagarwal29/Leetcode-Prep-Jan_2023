# Return the minimum cost to fly every person to a city such that exactly 
import math

def two_city_Scheduling(costs):
    # appending the difference between costs and their actual cost
    difference = []

    for cost1, cost2 in costs:
        difference.append([cost1 - cost2, cost1, cost2])

    difference.sort() # sort the array according to the differences 
    min_cost =0
    for i in range(len(difference)):
        if i < math.floor(len(difference)/2):
            min_cost += difference[i][1]
        else:
            min_cost += difference[i][2]

    return min_cost

if __name__=="__main__":
    
    costs = [[10, 20], 
            [30, 200], 
            [400, 50], 
            [30, 20]]

    print(two_city_Scheduling(costs=costs))




