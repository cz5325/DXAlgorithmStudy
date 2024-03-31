location = list(input())

# location[0] location[1]

dy = [-2, -2, 2, 2, -1, 1, -1, 1]
dx = [-1, 1, -1, 1, -2, -2, 2, 2]


count = 0
for i in range(len(dx)):
    row = int(location[1])
    col = ord(location[0])
    row += dx[i]
    col += dy[i]
    if (row>=1 and row<=8) and (col>=ord('a') and col<=ord('h')):
        count += 1
print(count)