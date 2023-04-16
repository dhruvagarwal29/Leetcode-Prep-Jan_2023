# Try to solve the N-th Tribonacci Number problem.

# get the nth tribonacci number 

def tribonacci(n):
    if n < 3 and n >1:
        return 1 
    elif n ==0 : return 0

    dp = [0] * (n+1)

    dp[0] = 0
    dp[1] = 1 
    dp[2] = 1 

    for i in range(n+1):
        if i >= 3:
            dp[i]= dp[i-3]+dp[i-2]+dp[i-1]

    return dp[-1] 

if __name__ == "__main__":
    n = 7
    print(tribonacci(n))