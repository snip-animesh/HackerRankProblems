amount,n=map(int,input().split())
coins=[int(x) for x in input().split()]

dp=[1]+[0]*amount

for coin in coins:
    for j in range(coin,amount+1):
        dp[j]+=dp[j-coin]
print(dp[amount])

# This is a dynamic Algorithm problem.
# https://www.hackerrank.com/challenges/coin-change/problem
