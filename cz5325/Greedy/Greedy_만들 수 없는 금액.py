N = int(input())
nums = list(map(int, input().split()))
nums.sort()  
 
target = 1
for num in nums:
    if target >= num:
        target += num
 
print(target)

# 만들 수 있는 최솟값인 1을 target에 선언
# target보다 다음 동전의 금액이 작거나 같다면, target에 그 동전의 금액을 더하기
# 만약 target보다 다음 동전의 금액이 크다면, target이 만들 수 없는 최소 금액