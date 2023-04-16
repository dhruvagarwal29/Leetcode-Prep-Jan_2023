# min number of boats required to transfer the person 

def boats(people, limit):
    # sort the people array as it contains weight of the people
    people.sort()

    lightest_person = 0
    heaviest_person = len(people) -1 
    no_of_boats = 0

    while lightest_person <= heaviest_person:
        no_of_boats +=1
        if people[lightest_person] + people[heaviest_person] <= limit:
            
            lightest_person+=1
            heaviest_person-=1
        else:
            heaviest_person-=1
        
    return no_of_boats

if __name__ == "__main__":

    people = [3,1,4,2,4]
    limit = 4

    result = boats(people, limit)

    print(result)