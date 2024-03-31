# 자릿수 기준 점수 N을 반으로 나누어 각각의 합이 같을 경우 LUCKY, 아니면 READY
# N은 항상 짝수
# 길이를 반으로 나누어 풀이

N = input()

x = 0 #앞부분
for i in range(len(N)//2):
    x += int(N[i])

y = 0 #뒷부분
for i in range(len(N)//2, len(N)):
    y += int(N[i])

if x == y:
    print("LUCKY")
else:
    print("READY")