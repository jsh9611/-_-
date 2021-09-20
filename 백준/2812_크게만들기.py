class Stack(list):
    push = list.append # push
    pop = list.pop # pop
    
    def is_empty(self):
        if not self:
            return True
        else:
            return False

import sys
# input = sys.stdin.readline

n, k = map(int, input().split())
nums = input()[::-1]

stack = Stack()

for item in nums:
    stack.push(item)

print(stack)