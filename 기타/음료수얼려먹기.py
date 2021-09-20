# 얼음틀 세로N, 가로M

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# dfs로 특정한 도르르 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위 외의 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 해당 노드를 방문처리한다
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상하좌우 위치도 재귀적으로 호출한다.
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

# 모든 위치에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1

print(result)