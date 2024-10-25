def solution(n, money):
    dp =[1] + [0]*n
    #print(dp)
    for coin in money :
        for price in range(coin,n+1):
            if price >=coin :
                dp[price] += dp[price-coin]
                #print(dp)
    return dp[n]% 1000000007