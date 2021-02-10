#왕실의 나이트
#구현
data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1 #아스키 코드 값 만큼 빼준다.

# 나이트가 움직일 수 있는 경우의 수
cases = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

result = 0
for case in cases:
    next_row = row + case[0]
    next_col = col + case[1]
    # 해당 위치로 이동이 가능한 경우
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1
print(result)