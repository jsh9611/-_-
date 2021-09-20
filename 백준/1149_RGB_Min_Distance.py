# 1149_RGB_Min_Distance.py
n = int(input())

cost = []
sum  = [[0, 0, 0] for _ in range(n)]

for _ in range(n):
    cost.append(list(map(int, input().split())))

sum[0] = cost[0][:]

for i in range(n-1):
    sum[i+1][0] = cost[i+1][0] + min(sum[i][1], sum[i][2])
    sum[i+1][1] = cost[i+1][1] + min(sum[i][0], sum[i][2])
    sum[i+1][2] = cost[i+1][2] + min(sum[i][0], sum[i][1])

print(min(sum[n-1][0], sum[n-1][1], sum[n-1][2]))