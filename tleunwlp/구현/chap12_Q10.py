# 0이 홈 부분, 1이 돌기 부분
def rotation(key):
    m = len(key)
    result = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m): # 회전시킨 key 배열 result 변수에 집어넣음
        for j in range(m):
            result[j][m-i-1] = key[i][j]
    return result
def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    # lock 길이의 3배인 배열을 만들어서 lock_lst에 저장
    lock_lst = [[1 for _ in range(n*3)] for _ in range(n*3)]
    key_lst = key
    for i in range(n):
        for j in range(n):
            lock_lst[i+n][j+n] = lock[i][j]
    lock_lst_cpy = lock_lst.copy()
    for _ in range(4): # 회전 4번의 경우 모두 다 탐색
        key_lst = rotation(key_lst)
        for i in range(len(lock_lst)-m+1):
            for j in range(len(lock_lst)-m+1):
                lock_lst_cpy = lock_lst.copy()
                for x in range(m):
                    for y in range(m):
                            lock_lst_cpy[x+i][y+j] += key_lst[x][y]
                for x in lock_lst:
                    if 0 not in x:
                        answer = True
                        return answer
    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))