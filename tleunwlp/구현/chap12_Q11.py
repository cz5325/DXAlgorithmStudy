n = int(input()) # 보드 수 n*n
k = int(input()) # 사과 수
apple_location = []
for _ in range(k):
    apple_location.append(list(map(int, input().split())))
l = int(input()) # 뱀의 방향 변환 횟수
dx = [0, 1, 0, -1] # 서남동북 순서
dy = [1, 0, -1, 0] # 서남동북 순서
direction = 0
second = 0
direction_x = []
direction_c = []
for _ in range(l):
    x, c = input().split()
    direction_x.append(int(x))
    direction_c.append(c)

def make_map(n, apple):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(apple)):
        a, b = apple[i][0], apple[i][1]
        result[a-1][b-1] = 1
    return result

def turn(direct):
    # 오른쪽과 왼쪽에 따라 방향 바꾸기
    global direction
    if direct == 'D':
        direction += 1
    elif direct == 'L':
        direction -= 1
    if direction == 4:
        direction = 0
    elif direction == -1:
        direction = 3
    return direction

arr = make_map(n, apple_location)
snake = [[0 for _ in range(n)] for _ in range(n)]
snake[0][0] = 1
snake_x = 0
snake_y = 0
tail_location = [(0, 0)]
while True:
    next_x = snake_x + dx[direction]
    next_y = snake_y + dy[direction]
    # 다음 칸이 이러하면 게임 끝.
    if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n or snake[next_x][next_y] == 1:
        second += 1
        break
    # 이동한 칸에 사과 있다면 사과는 없어지고 꼬리 움직이지 않음. 즉, 몸 길이 늘어남
    if arr[next_x][next_y] == 1:
        arr[next_x][next_y] = 0
    # 사과 없다면 몸길이 줄여서 꼬리가 위치한 칸 줄여준다. 즉, 몸길이는 변하지 않음 !!
    else:
        tail_x, tail_y = tail_location.pop(0)
        snake[tail_x][tail_y] = 0
    # 몸길이 늘려서 머리를 다음 칸에 위치
    snake_x = next_x
    snake_y = next_y
    snake[snake_x][snake_y] = 1
    tail_location.append((snake_x, snake_y))
    # 이 단계 거칠 때마다 초 증가
    second += 1

    # 방향 변환 정보 주어지면 방향 회전
    if second in direction_x:
        sec_idx = direction_x.index(second)
        sec_direction = direction_c[sec_idx]
        direction = turn(sec_direction)

print(second)

