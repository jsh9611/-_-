# 미로 탈출
# N x M 크기의 직사각형 형태의 미로에서 탈출한다
# (1,1)에서 시작하여 (N,M)으로 탈출해야 한다.
# BFS 활용

from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
graph = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 
1]]

# 이동할 네 방향 정의(동 서 남 북)
dx = [1, -1, 0,  0]
dy = [0,  0, 1, -1]

# BFS 소스코드 구현
def bfs(x, y):
    # deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        print(graph)
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치를 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리를 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리를 반환
    return graph[n-1][m-1]

# BFS를 수행한 결과 출력
print(bfs(0,0))
print(graph)