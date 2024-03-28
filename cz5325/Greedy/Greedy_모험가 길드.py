#모험가길드
N = int(input())
data = list(map(int,input().split()))
data.sort()
 
group_cnt = 0     # 그룹 수
traveler = 0     # 현재까지 확인한 모험가의 수
 
for i in data:
    traveler += 1
    if traveler >= i:
        group_cnt += 1  # 그룹 수
        traveler = 0    # 초기화 후 반복
 
print(group_cnt)
 

# traveler에 1을 더하여 현재까지 확인한 모험가의 수를 업데이트
# 만약 traveler가 현재 확인한 모험가의 공포도보다 크거나 같다면, 이 모험가를 포함한 그룹을 만들 수 있으므로 group_cnt를 1 증가시키고, traveler를 0으로 초기화하여 다음 그룹을 위한 준비
# 반복문이 끝나면 최대 그룹 수인 group_cnt를 출력