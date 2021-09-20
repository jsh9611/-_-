# 2156_Drink_Wine.py
import sys
read = sys.stdin.readline

n = int(read())

dp = [0]*(n+3)
v = [0]*(n+3)

for i in range(n):
    v[i+1] = int(read())

dp[1] = v[1]
dp[2] = dp[1]+v[2]

for i in range(3,n+1): 
    dp[i] = max(dp[i-1], dp[i-2] + v[i], dp[i-3] + v[i-1] + v[i])
    # dp[i] = dp[i-3] + v[i-1] + v[i]   # 마지막에 둘 다 마시는 경우
    # dp[i] = max(dp[i], dp[i-2] + v[i])# 마지막에 한번만 마시는 경우
    # dp[i] = max(dp[i], dp[i-1])         # 마지막에 안마시는 경우
print(dp[n])