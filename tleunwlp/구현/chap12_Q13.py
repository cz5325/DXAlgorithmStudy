from itertools import combinations
n, m = map(int, input().split())
city = []
# 0 빈칸, 1 집, 2 치킨집
for _ in range(n):
    city.append(list(map(int, input().split())))

def select_m(arr):
    # 치킨집 중에서 m개를 고를 치킨집의 위치를 변수에 저장
    m_lst = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                m_lst.append([i, j])
    return m_lst

def select_house(arr):
    # 집이 있는 위치를 house 변수에 저장
    house = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                house.append([i, j])
    return house

def chicken_distance(chicken_arr, house_arr):
    # 치킨거리 계산하는 함수
    distance = 0
    for house in house_arr:
        house_x = house[0]
        house_y = house[1]
        min_dist = 1000
        for chicken in chicken_arr:
            chicken_x = chicken[0]
            chicken_y = chicken[1]
            temp = abs(chicken_x - house_x) + abs(chicken_y - house_y)
            if min_dist > temp:
                min_dist = temp
        distance += min_dist
    return distance

def solution(arr):
    m_cases = combinations(select_m(arr), m)
    house = select_house(arr)
    min_dist = 10000
    for m_case in m_cases:
        dist = chicken_distance(m_case, house)
        if min_dist > dist:
            min_dist = dist
    return min_dist

print(solution(city))