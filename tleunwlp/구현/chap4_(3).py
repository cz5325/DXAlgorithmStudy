import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b, d = map(int, input().split())
d_list = [3, 0, 1, 2] # 왼쪽 방향 리스트
dx = [-1, 0, 1, 0] # 방향 별 x 이동
dy = [0, 1, 0, -1] # 방향 별 y 이동
system = []
count = 1

for _ in range(n):
    system.append(list(map(int, input().split())))

visited = [[False if value == 0 else True for value in row] for row in system]

row = a
col = b
direction = d_list[d] # 왼쪽 방향 회전
# manual 작성
while True:

    if False not in visited:
        break

    if not visited[row + dx[direction]][col + dy[direction]]: # 가보지 않은 칸 존재
        if system[row + dx[direction]][col + dy[direction]] == 0: # 가보지 않은 칸 중 육지
            row += dx[direction]
            col += dy[direction]
            count += 1
            visited[row][col] = True
    else:
        direction = d_list[direction]

    if direction == d or visited[row + dx[direction]][col + dy[direction]]: # 바다인 칸 & 모두 다 가본 칸
        if system[row][col] != 1:  # 뒤쪽 방향이 바다가 아니라면
            if direction == 0:
                row += 1
            elif direction == 1:
                col -= 1
            elif direction == 2:
                row -= 1
            elif direction == 3:
                col += 1
        else:
            break
print(count)