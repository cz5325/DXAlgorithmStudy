
def solution(n, build_frame):
    answer = []
    pillar_full = [[0 for _ in range(n+1)] for _ in range(n+1)]
    b_full = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for li in build_frame:
        x, y, a, b = li[0], li[1], li[2], li[3]
        if a == 0: # 구조물이 기둥이면
            if b == 1: # 기둥을 설치하면
                # 기둥이 바닥 위 또는 보의 한쪽 끝부분 또는 다른 기둥 위에 있는 조건
                if y == 0 or b_full[x][y] == 1 or pillar_full[x][y] == 1:
                    pillar_full[x][y] += 1
                    pillar_full[x][y+1] += 1
                    answer.append([x, y, a])
            else: # 기둥을 삭제하면
                # 기둥을 삭제할 수 있는 조건
                if b_full[x][y+1] == 0 or pillar_full[x][y+1] == 1:
                    pillar_full[x][y] -= 1
                    pillar_full[x][y+1] -= 1
                    answer = [item for item in answer if item != [x, y, a]]

        else: # 구조물이 보면
            if b == 1: # 보를 설치하면
                # 한쪽 끝부분이 기둥 위에 있거나, 양쪽 끝부분이 다른 보와 동시에 연결되어야 할 조건
                if (pillar_full[x][y] == 1 or pillar_full[x+1][y] == 1) or (b_full[x][y] == 1 and b_full[x+1][y] == 1):
                    b_full[x][y] += 1
                    b_full[x+1][y] += 1
                    answer.append([x, y, a])
            else: # 보를 삭제하면
                # 보를 삭제할 수 있는 조건
                if pillar_full[x][y] == 0 and pillar_full[x+1][y] == 0 and (b_full[x][y] != 2 and b_full[x+1][y] != 2):
                    b_full[x][y] -= 1
                    b_full[x+1][y] -= 1
                    answer = [item for item in answer if item != [x, y, a]]

    sorted_answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return sorted_answer

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))