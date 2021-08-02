import sys
n = int(sys.stdin.readline())

time = []
for i in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))
scd = sorted(time, key=lambda x: -x[1])  
print(scd)

ans = scd[0][1]-scd[0][0]

for i in range(1,n):
    if ans>scd[i][1]:
        ans = scd[i][1]-scd[i][0]
    else:
        ans = ans - scd[i][0]
print(ans if ans>=0 else -1)

    # else:
    #     print(scd[0][1]-scd[0][0])

    # if scd[0][1]-scd[0][0]<left:
    #     print(scd[0][1]-scd[0][0])
    # elif left < 0:
    #     print(-1)
    # else:
    #     print(left)
"""
4
3 5
8 14
5 20
1 16
=>2

3
4 5
1 5
2 20
=>0

3
1 2
1 2
3 2
=>-1

3
1 1
2 2
3 3
=>-1


"""
# import sys
# N = int(input())
# arr = []
# for _ in range(N):
#     a, b = map(int, sys.stdin.readline().split())
#     arr.append((b, a))
# # 가장 늦은 시간에 해결해도 되는 일 순으로 역순 정렬
# arr.sort(reverse=True)
# print(arr)

# 15
# 14
# 6
# 3
