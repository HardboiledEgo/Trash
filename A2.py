k=list(str(input()).split())
u=list(str(input()).split())
sum_el=0
answer=0

n=int(k[0])
e=int(k[1])

for el in u:
    sum_el+=int(el)

if sum_el%e!=0:
    answer+=1

answer+=sum_el//e

print(answer)