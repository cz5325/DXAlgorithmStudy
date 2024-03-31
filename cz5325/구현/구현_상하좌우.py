# (1,1) 시작 
# L: 좌, R: 우, U: 위, D: 아래

# 내 풀이(오답)
# n = int(input())
# move = list(map(str, input().split())) 
# x,y = 1,1

# for i in move:
#     if i == 'R':
#         y += 1
#     elif i == 'L':
#         y -= 1
#     elif i == 'U':
#         x -= 1
#     elif i == 'D':
#         x += 1
# print(x, y)


# 정답

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]   
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동한 위치로 업데이트
    x, y = nx, ny
        
print(x, y)
