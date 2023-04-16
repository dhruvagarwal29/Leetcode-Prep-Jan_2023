# any number is happy number if repeatedly replacing it with a number 
# equal to " sum of th sqaure of all of its digits, leads us to number 1" 

def find_happy_number(num):
    slow = num 
    fast = num 

    while True:
        slow = find_square_sum(slow) # move one step
        fast = find_square_sum(find_square_sum(fast)) # move two steps

        if slow == fast: # found cycle means sum of square is not 1 in this number
            break  
    
    return slow == 1

def find_square_sum(num):
    # eg 23 came 
    sum = 0
    while num > 0:
        digit = num % 10  # getting the ones position digit  (23 % 10 = 3) 
        sum += digit * digit # making the sum of square of digit  ( sum = 3*3 = 9)
        num = num // 10   # reducing the digit                     ( num = 23 //10 = 2)
    return sum  

def main():
    print(find_happy_number(23))
    print(find_happy_number(12))

main()