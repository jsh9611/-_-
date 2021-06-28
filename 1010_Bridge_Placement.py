# 1010_Bridge_Placement.py

count = int(input())

# bridge = [[0]*(m+1) for j in range(n+1)]
bridge = [[0]*(31) for j in range(31)] 

for _ in range(count):
    n,m = map(int, input().split())    

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i>j:
                continue
        
            if i==1:
                bridge[i][j] = j
            elif i==j:
                bridge[i][j] = 1
            else: # n>2
                if bridge[i][j] != 0:
                    continue
                temp = 0
                for k in range(i,j+1):
                    temp += bridge[i-1][k-1]  # 2,3 => 1,1 + 1,2
                bridge[i][j] = temp
    print(bridge[n][m])
