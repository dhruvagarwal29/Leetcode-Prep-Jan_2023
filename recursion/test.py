# testing recursion 

def printing(num,count):
    
    print(num)
    count+=1
    if count < 10:   
        printing(num,count)


if __name__=="__main__":
    num = 1
    count = 0
    printing(1, count)