# 11726_2xn_Tiling.py
import sys
n = int(sys.stdin.readline().rstrip())

f = [0]*(n+1)

f[0] = 1
f[1] = 2

for i in range(2,n):
    f[i] = f[i-2] + f[i-1]

print(f[n-1]%10007)