import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b, d = map(int, input().split())
dx = [-1, 0, 1, 0] # 북동남서 방향 별 x 이동
dy = [0, 1, 0, -1] # 북동남서 방향 별 y 이동
system = []
count = 1

for _ in range(n):
    system.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]
visited[a][b] = 1

direction = d # 처음 주어진 방향

def turn():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# manual 작성
turn_time = 0
while True:
    turn()
    turn_x = a + dx[direction]
    turn_y = b + dy[direction]
    # 가보지 않은 칸이 존재한다면
    if visited[turn_x][turn_y] == 0:
        # 그 가보지 않은 칸이 육지라면
        if system[turn_x][turn_y] == 0:
            visited[turn_x][turn_y] = 1
            a = turn_x
            b = turn_y
            turn_time = 0
            count += 1
    # 가보지 않은 칸이 없다면
    else:
        turn_time += 1
    # 만약 네 방향 모두 가본 칸이라면
    if turn_time == 4:
        # 그 뒤의 칸이 육지라면
        turn_x = a - dx[direction]
        turn_y = b - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if system[turn_x][turn_y] == 0:
            a = turn_x
            b = turn_y
            turn_time = 0
        # 바다라면 이동 못함
        else:
            break
print(count)