# You need to return the minimum number of boats to carry every person in the array.

def min_boats(arr,limit):
    min_boats = 0
    arr.sort() # sort the array and use two pointers (lightest and heaviest)
    
    lightest = 0
    heaviest = len(arr)-1

    while lightest <= heaviest:
        min_boats+=1
        if arr[lightest]+arr[heaviest]<=limit:  # checking the limit if add the light and heavy element 
            # can equal to or less than limit then we can move out lightest pointer ahead 
            # else put the heaviest element in the array and decrease the count
            lightest+=1
        
        heaviest-=1

    return min_boats

if __name__=="__main__":
    arr= [2,1,1]
    limit = 3

    print(min_boats(arr,limit))