# 백준 1051번 숫자 정사각형
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(input().rstrip()))

s_len = 0
for i in range(n):
    for j in range(m):
        for k in range(j+1,m):
            if arr[i][j] == arr[i][k]:
                temp = k-j
                if i+temp<n:
                    if arr[i+temp][j] == arr[i+temp][k] == arr[i][j]:
                        s_len = max(s_len, temp)
print((s_len+1)**2)