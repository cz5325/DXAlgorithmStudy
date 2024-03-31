score= str(input())

score=list(score)

cut= int(len(score)/2)

num1=0
num2=0

for i in range(0,cut):
    num1=num1+int(score[i])
for i in range(cut,len(score)):
    num2=num2+int(score[i])

if num1==num2:
    print('LUCKY')
else:
    print('READY')
