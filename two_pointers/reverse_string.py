#Given a sentence, reverse the order of its words without 
# affecting the order of letters within a given word.

# string - hello world
# reverse string - world hello 

def reverse_string(string):

    # reverse the string 
    string_rev=""
    for i in string:
        string_rev = i + string_rev
    # print(string_rev)
    left = 0
    right = 0

    # now after reversing the string loop it over the first word and reverse it again 
    counter = 0
    while True:
        while left <len(string) and string_rev[left] == " ":
            left +=1
        
        if left == len(string):
            break

        right = left + 1
        while right < len(string) and string_rev[right] != " ":
            end+=1
        
        rev(string_rev, left, right)
        left = right
    return string_rev 
def rev(stri, start, end):

    while start < end:
        temp = stri[start]
        stri[start] = stri[end]
        stri[end]= temp 

        start +=1 
        end -=1

if __name__ =="__main__":
    string = "Hello World"

    print(reverse_string(string))
