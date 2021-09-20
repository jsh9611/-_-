import time, random

# 수행시간 O(n)
def evaluate_n1(A, x):
    n = len(A)
    sum = 0
    expo = [1]*n
    for i in range(n-1):
        expo[n-2-i] = expo[n-1-i]*x
    for j in range(n):
        sum += A[j]*expo[j]
    return sum

# 수행시간 O(n^2)
def evaluate_n2(A, x):
    n = len(A)
    sum = 0
    expo = [1]*n
    for i in range(n):
        for j in range(i):
            expo[n-1-i] *= x
    for j in range(n):
        sum += A[j]*expo[j]
    return sum
	
random.seed()		# random 함수 초기화

# n 입력받음
n = int(input())

# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
# n-1차 방정식의 n개의 계수 랜덤생성해 배열에 추가
A = []
for i in range(n):
	A.append(random.randint(-1000, 1000))

# 무작위 x값 대입
x = random.randint(-1000, 1000)

# evaluate_n1 호출
before = time.process_time()      # 현재 시간을 얻는다
print(evaluate_n1(A, x))
after = time.process_time()       # 현재 시간을 
time_n1 = after - before      # 함수 호출 전과 후의 시간 차이 (= 함수 수행시간)

# evaluate_n2 호출
before = time.process_time()      # 현재 시간을 얻는다
print(evaluate_n2(A, x))
after = time.process_time()       # 현재 시간을 얻는다
time_n2 = after - before      # 함수 호출 전과 후의 시간 차이 (= 함수 수행시간)
# 두 함수의 수행시간 출력

print('tiem_n1:',time_n1)
print('tiem_n2:',time_n2)

"""
알고리즘 과제#1 
수행시간 체험 - 다항식 계산

n의 개수가 1 천개일때는 실행시간의 차이가 거의 없었다 
하지만 n 의 크기가 커지면 커질수록 시간이 격차가 기하급수적으로 벌어지기 시작하였다 
심지어 n 이 10 000 이 되었을 무렵부턴 제한시간 60 초가 넘어가 구름에서 실행이 불가능하였다
이번 과제를 통해 코드의 효율성이 얼마나 중요한지를 다시 한 번 일깨워 주는 계기가 되었다
"""