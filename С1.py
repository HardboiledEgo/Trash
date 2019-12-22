k=int(input())
u=list(str(input()).split())
a=[]
sum_el=0

for el in u:
    a.append(int(el))
    
for i in range(k-1):
    for j in range(k-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

for el in a:
    sum_el+=el

sum_el_a=sum_el/5
sum_el_b=0

i=0
kon=0

if sum_el%5==0:
    while kon<5:
        while sum_el_b<sum_el_a and i<k:
            sum_el_b+=a[i]
            i+=1
        if sum_el_b==sum_el_a:
            kon+=1
        else:
            break
        sum_el_b=0

if kon==5:
    print('Yes')
else:
    print('No')