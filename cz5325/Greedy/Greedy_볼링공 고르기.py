# 정답
n, m = map(int, input().split())
data = list(map(int, input().split()))
 
array = [1
  ] * 10  # 각 무게의 볼링공이 몇 개 있는지를 카운트하는 리스트를 생성( 배열 )
 
for x in data:
 
    array[x] += 1   # 입력받은 볼링공의 무게를 기준으로 무게별로 카운트
 
result = 0 # 결과 초기화
 
for i in range(1, m+1):
    n -= array[i]   # 선택할 수 있는 볼링공의 수는 현재 총 볼링공의 수에서 현재 무게의 볼링공의 수를 뺀 값
    result += array[i] * n # 현재 무게의 볼링공을 선택할 경우, 다른 무게의 볼링공과의 조합 수를 곱해서 결과에 더한다
 
print(result)

# 다른 방법
N, M = map(int, input().split())
 
K = list(map(int, input().split()))
 
result = 0
 
for i, j in enumerate(K):
  for k in K[i+1:]:
    if j == k:
      continue
    else:
      result += 1
 
print(result)
 
# [출처] 이코테 파트 3 파이썬 문제 풀이 및 내가 생각한 답, 05.볼링공 고르기|작성자 passgiant

