import sys
n = int(sys.stdin.readline())

time = []
for i in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))
time.sort()    

count = 0
skip = 0
for i in range(n):
    if time[i][0] < skip:
        if time[i][1] < skip:
            skip = time[i][1]
        continue
    skip = time[i][1]
    count += 1
print(count)