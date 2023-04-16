#For any n positive number in base 10, return the complement of
#  its binary representation as an integer in base 10
from math import floor, log2
def base10(num):
    if num == 0:
        return 1

    # counting the number of bits required by this number in binary representation
    count_bit = floor(log2(num)) + 1

    # computing all bits set of the number
    all_digit = pow(2,count_bit) - 1

    # now flipping all bits of number by taking xor with all_bits_set

    return num ^ all_digit
 
if __name__=="__main__":
    num = 8
    print(base10(num))