import sys
from collections import deque

def bfs(x,y):
    # deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))

    # 방문을 한 경우 2를 대입
    global count
    graph[x][y] = 2

    count += 1

    # queue가 빌 때 까지
    while queue:
        x,y = queue.popleft()
        # 현재 위치로 부터의 8가지 방향을 확인
        for i in range(8):
            # nx,ny에 x,y 다음에 올 좌표를 대입
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖인 경우 무시
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            # 벽을 만난 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 처음 방문한 경우 2를 대입해 방문처리
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                queue.append((nx,ny))
    return count

while True:
    # n x m 크기의 미로
    n, m = map(int, sys.stdin.readline().split())

    # n과 m에 0을 받는 경우 종료한다
    if n == 0 and m == 0:
        break

    # 입력을 2차원 리스트에 저장(0은 바다, 1은 땅, 2는 방문한 땅)
    graph = []
    for i in range(m):
        graph.append(list(map(int, sys.stdin.readline().split())))

    # 8가지 방향
    dx = [1,0,-1,0,1,1,-1,-1]
    dy = [0,1,0,-1,1,-1,1,-1]

    # 섬의 갯수
    count = 0
    result = 0

    # 땅인 경우에 bfs함수 실행
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                result = bfs(i,j)
    
    print(result)