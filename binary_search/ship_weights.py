def shipWithinDays(weights, D):
    max_capacity = max(weights)
    total_weight = sum(weights)

    for capacity in range(max_capacity, total_weight + 1):
        days = 1
        current_load = 0

        for weight in weights:
            if current_load + weight <= capacity:
                current_load += weight
            else:
                days += 1
                current_load = weight

        if days <= D:
            return capacity

    return total_weight

if __name__=="__main__":
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    
    print(shipWithinDays(weights, days))
