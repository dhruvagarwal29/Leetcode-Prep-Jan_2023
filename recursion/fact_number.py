# give me the factorial of the number

def fact(n):
    if n==0:
        return 1
    
    return n * fact(n-1)


if __name__=="__main__":

    num = 5
    print(fact(num))