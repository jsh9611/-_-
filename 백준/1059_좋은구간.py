# 1059_좋은구간.py
import sys
input=sys.stdin.readline
from collections import deque

def nice(l,s,n):
    if n in s:
        return 0
    if n<s[0]:
        return (s[0]-n)*n-1
    for i in range(l):
        if s[i]>=n:
            a = s[i-1]
            b = s[i]
            return (b-n)*(n-a)-1

l = int(input())
s = list(map(int,input().split()))
s.sort()
n = int(input())

result = nice(l,s,n)
if result<0:
    print(0)
else:
    print(result)