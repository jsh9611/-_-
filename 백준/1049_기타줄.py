import sys
n, m = map(int, sys.stdin.readline().split())

strings = []
for i in range(m):
    strings.append(list(map(int, sys.stdin.readline().split())))
pack = sorted(strings, key = lambda x:x[0])
single = sorted(strings, key = lambda x:x[1])

sum = 0
if pack[0][0] > single[0][1]*6:
    sum += single[0][1]*n
else:
    sum += pack[0][0]*(n//6)
    if pack[0][0] < single[0][1]*(n%6):
        sum += pack[0][0]
    else:
        sum += single[0][1]*(n%6)
print(sum)