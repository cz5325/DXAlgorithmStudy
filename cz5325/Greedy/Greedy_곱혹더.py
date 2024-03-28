# 내 풀이
S = list(map(int, input()))
 
nums = 1
for num in S:
    if num == 0 or num == 1:
        nums += num 
    else:
        nums *= num
        
print(nums)
# 0과 1인 경우를 제외하면 곱하기가 유리
# ex) 129이면 (1+2)*9 = 27, 1*2*9 = 18 
# 곱하기 할 경우를 생각해 nums를 0이 아닌 1로 지정

# 다른 방법
data = input()
 
result = int(data[0])
 
for i in range(1, len(data)):
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num
 
print(result)
