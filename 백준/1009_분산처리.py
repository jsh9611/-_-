import sys
input = sys.stdin.readline
t = int(input())

com = []

nums = [[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1],[10]]
for i in range(t):
    a,b = map(int,input().split())
    a = a%10
    print(nums[a-1][b%len(nums[a-1])-1])