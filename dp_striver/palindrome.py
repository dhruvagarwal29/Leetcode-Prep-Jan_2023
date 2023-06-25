# palindrome 

def palin(str):
    i = 0
    j= len(str) -1 

    while i < j:
        if str[i] == str[j]:
            i+=1
            j-=1
        else:
            return False
    
    return True


if __name__=="__main__":
    str = "abaa"

    print(palin(str))