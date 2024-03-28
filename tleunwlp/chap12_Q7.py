n = list(input())

n_divide = len(n) // 2
sum1 = 0
sum2 = 0
for i in range(n_divide):
    sum1 += int(n[i])
for i in range(n_divide, len(n)):
    sum2 += int(n[i])
if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')