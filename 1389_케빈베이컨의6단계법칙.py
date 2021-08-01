import sys

n, m = map(int, sys.stdin.readline().split())

INF = 10000 # 연결이 끊긴 경우
graph = [[INF]*n for _ in range(n)]

# 무방향 그래프이기 때문에 출발과 도착을 서로 연결한다
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1 
    graph[b-1][a-1] = 1

# 플로이드-와샬
# k = 거쳐가는 노드
for k in range(n):
    # i = 출발 노드
    for i in range(n):
        # j = 도착 노드
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 각 노드가 부담하게 될 총 비용을 더한다.
sum = [0]*n
for i in range(n):
    for j in range(n):
        sum[j] += graph[i][j]

# 비용이 가장 적은 노드중 index가 가장 작은 것을 구한다
print(sum.index(min(sum))+1)