import sys

n,k = map(int, input().split()) 

coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))

count = 0
for i in range(n-1, -1, -1):
    if k==0: break
    quotient = k//coin[i]
    if quotient>0:
        count += quotient
        k -= coin[i]*quotient

print(count)