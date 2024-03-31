n = int(input())
answer = 0
lst = [500, 100, 50, 10]
 
for i in lst:
  answer += n // i
  n %= i
 
print(answer)
 
# 1260
# 6