# 2178_maze.py
import sys
from collections import deque

# n x m 크기의 미로
n, m = map(int, sys.stdin.readline().split())
# 2차원 리스트에 저장
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# # 4가지 방향
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    # deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # queue가 빌 때 까지
    while queue:
        x,y = queue.popleft()
        # 현재 위치로 부터의 4가지 방향을 확인
        for i in range(4):
            # nx,ny에 x,y 다음에 올 좌표를 대입
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖인 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            # 벽을 만난 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 노드를 처음 방문할 경우 최단거리를 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))