import sys
import heapq
n = int(sys.stdin.readline())

scd = []
for i in range(n):
    scd.append(list(map(int, sys.stdin.readline().split())))
scd.sort()  

heap = []

heapq.heappush(heap, scd[0][1])
for i in range(1,n):
    if scd[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, scd[i][1])
    heap.append(scd[i][1])
print(len(heap))