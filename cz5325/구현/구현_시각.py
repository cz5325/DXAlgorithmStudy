# 00시부터 N시 까지의 시각 중 3이 하나라도 포함되는 경우의 수 구하기
# 시, 분, 초를 3중 반복문으로 나누어 계산 (완전탐색법)

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 3이 포함되어 있으면 카운트
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)