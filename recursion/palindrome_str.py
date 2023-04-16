# WAP to find a palindrome of a function 

def palindrome(i, str):
    n = len(str)
    if i >= n/2:
        return True

    if str[i] != str[n-i-1]:
        return False

    return palindrome(i+1, str)

def main():
    str = "MADAM"
    str1 = [1,2,2,1]
    print(palindrome(0,str))
    print(palindrome(0,str1))

main()