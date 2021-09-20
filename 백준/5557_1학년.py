import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print((sum(arr[:n-1])-arr[-1])/2)

# 합쳐서 19가 되게 만드는 경우의 수