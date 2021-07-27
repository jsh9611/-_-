# 플로이드 와샬(Floyd Warshall) 알고리즘
import sys

n = int(sys.stdin.readline())

INF = 10000
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))  
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF

# k = 거쳐가는 노드
for k in range(n):
    # i = 출발 노드
    for i in range(n):
        # j = 도착 노드
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n):
    for j in range(n):
        if graph[i][j] >= INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
            # print(graph[i][j], end=' ') # 최단 경로 비용
    print()