def gas_station(cost, gas):


    if sum(cost) > sum(gas):
        return -1

    starting_index = 0
    calculated_gas = 0
    for i in range(len(gas)):
        
        calculated_gas += gas[i]-cost[i]
        if calculated_gas < 0: # means if we dont have gas to go ahead 
            calculated_gas = 0 # reset the gas to 0
            starting_index = i+1
        
    return starting_index



if __name__=="__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    print(gas_station(cost, gas))
