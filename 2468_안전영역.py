import sys
from collections import deque

# n x n 크기의 지도
n = int(sys.stdin.readline())

# 2차원 리스트에 저장
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# # 4가지 방향
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y,temp,h):
    # deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))

    # 방문을 한 경우 -1를 대입
    global count
    temp[x][y] = -1

    count += 1

    # queue가 빌 때 까지
    while queue:
        x,y = queue.popleft()
        # 현재 위치로 부터의 4가지 방향을 확인
        for i in range(4):
            # nx,ny에 x,y 다음에 올 좌표를 대입
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖인 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            # 물에 잠긴 경우 무시
            if temp[nx][ny] <= h:
                continue
            # 처음 방문한 경우 -1를 대입해 방문처리
            if temp[nx][ny] > 0:
                temp[nx][ny] = -1
                queue.append((nx,ny))
    return count

max = 0
result = 0
for h in range(101):
    count = 0
    temp = [item[:] for item in graph]
    for i in range(n):
        for j in range(n):
            if temp[i][j] > h:
                result = bfs(i,j,temp,h)
    if result > max:
        max = result
print(max)