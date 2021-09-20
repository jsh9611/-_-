#게임 개발
# 구현

# N, M을 공백으로 구분하여 입력받는다
n, m = map(int, input().split())

# 방문한 위치를 지정할 기본 맵을 0으로 초기화
d = [ [0] * m for _ in range(n) ]
x, y, direction = map(int, input().split())
# 현재 좌표를 방문처리한다. (시작 위치는 육지라 가정)
d[x][y] = 1

# 전체 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북[0], 동[1], 남[2], 서[3]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction # 전역변수 이용
    direction -= 1
    if direction == -1:
        direction = 3

# 게임
count = 1
turn_time = 0
while True:
    turn_left() # 왼쪽으로 회전
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 가지 않았던 지역이 갈 수 있는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 후 가보지 않은 지역이 없거나 바다인 경우
    else:
        turn_time += 1
    # 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤에 바다로 막혀있다면
        else:
            break
        turn_time = 0

print(array)
print(d)
print(count)