a=list(str(input()))

lit_a=[]
it_a=[]

for i in range(0,len(a)):
    if ord(a[i])>=65:
        lit_a.append(a[i])
    else:
        it_a.append(a[i])

lit_a.sort()
it_a.sort()

hap=lit_a+it_a

for i in hap:
    print(i,end="")