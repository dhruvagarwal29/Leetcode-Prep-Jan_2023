# check whether the string is a valid palindrome or not

def valid_palindrome(str):
    left = 0
    right = len(str)-1

    while left < right:
        if str[left]==str[right]:
            left +=1
            right -=1
        else:
            return False 

    return True

if __name__ =="__main__":
    str = "abccba"
    str1 = "oyo"
    str2 = "Dhruv"
    print(valid_palindrome(str2))