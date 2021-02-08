# Chapter 04 구현
# 상하좌우

n = int(input())
data = list(input().split())

row = 1
col = 1

for plan in data:
    if plan == "L":
        row -= 1
    elif plan == "R":
        row += 1
    elif plan == "U":
        col -= 1
    elif plan == "D":
        col += 1
    else:
        print("Error!")
        break
    if row<1:
        row = 1
    if col<1:
        col = 1
    if row>n:
        row = n
    if col>n:
        col = n
print(col, row)