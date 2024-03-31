S = list(input())

S = sorted(S)
total = 0

for i in S:
    if i.isdigit():
        total += int(i)
    else:
        temp = S.index(i)
        break
S_result = S[temp:] + list(str(total))
print(''.join(S_result))