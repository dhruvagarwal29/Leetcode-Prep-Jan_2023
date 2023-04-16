# give me the sum of n numbers

# parameterized 
def sumation_parameterized(n, sum):
    if n == 0:
        print(sum)
        return
    else:
        sumation_parameterized(n-1, sum+n)
          

# functional 

def sumation_functional( num):
    if num==0:
        return 0
    
    return num + sumation_functional(num-1)



if __name__=="__main__":

    num = 3
    sum = 0
    sumation_parameterized(num, sum)
    print(sumation_functional(num))