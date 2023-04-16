# Coin Change

def coin_change(coin, total):
    
    for i in range(total+1):
        dp = 0 * i  # base case dp[0] = 0 if total is 0

    for i in range(coin):
        for j in range(coin[i]):

    
    


if __name__ == "__main__":
    coins = [1,2,3,4]

    total = 11

    min_coins = coin_change(coins, total)

    print(min_coins)

