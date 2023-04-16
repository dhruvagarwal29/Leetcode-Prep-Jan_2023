# print names n times using recursion 


def names(name, num):

    if num != 0:
        print(name)
        num -=1
        names(name, num)


if __name__=="__main__":
    num = 10
    names("Dhruv", num)