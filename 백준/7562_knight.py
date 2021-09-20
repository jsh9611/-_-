# 7562_chess.py
import sys
input=sys.stdin.readline
from collections import deque

# 8가지 이동 가능한 경우
dx = [1,1,-1,-1,2,2,-2,-2]
dy = [2,-2,2,-2,1,-1,1,-1]

def bfs(sx, sy, fx, fy):
    queue=deque()
    queue.append((sx,sy))
    while queue:
        # 큐에서 빼기
        x,y=queue.popleft()
        # 만약 시작점이랑 도착점이랑 같으면 출력하고 종료
        if x == fx and y == fy:
            print(board[fx][fy])
            break
        # 큐에서 pop한 좌표를 8방향 for문 돌려서 체크
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            # 범위 밖인지 체크
            if nx<0 or nx>=l or ny<0 or ny>=l:
                continue
            # 방문을 안했다면 입력
            if board[nx][ny] == 0:
                # 다음에 방문할 좌표를 추가
                queue.append((nx,ny))
                board[nx][ny] = board[x][y] + 1

# 테스트케이스 수 입력받기
t = int(input())
for i in range(t):
    # 체스판크기 입력받기
    l = int(input())
    # 시작점 도착점 입력받기
    sx, sy = map(int, input().split())
    fx, fy = map(int, input().split())
    # 체스판만큼 배열 만들기
    board=[[0]*l for i in range(l)]
    bfs(sx, sy, fx, fy)