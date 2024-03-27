# N: 배열의 크기, M: 숫자가 더해지는 횟수, K: 최대한 쓸 수 있는
N, M, K = map(int,input().split())
data = list(map(int,input().split()))
 
data.sort()             # 리스트 정렬
first = data[N - 1]     # 첫 번째 큰 수
second = data[N - 2]    # 두 번째 큰 수
 
result = 0
 
while True:
    for i in range(K): # 가장 큰 수를 K번 더하기
        if M == 0:
            break
        result += first
        M -= 1          # 더할 숫자의 횟수를 하나씩 줄여가는 역할
    if M == 0:
        break
    result += second
    M -= 1
 
print(result)