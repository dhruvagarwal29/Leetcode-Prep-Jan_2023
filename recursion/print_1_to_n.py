# print(1 to n)

def print_1_to_n(count, n):

    if count <= n:
        print(count)
        count +=1 
        print_1_to_n(count, n)

def print_n_to_1(count, n):

    if n >= count:
        print(n)
        n -=1 
        print_n_to_1(count, n)        

if __name__=="__main__":
    count = 0
    n = 10
    # print_1_to_n(count , n)
    print_n_to_1(count, n)