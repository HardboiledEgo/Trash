k=int(input())
u=list(str(input()).split())
sch=0
a=[]

for el in u:
    a.append(int(el))
    
for i in range(k-1):
    for j in range(k-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            sch+=1
#print(a)
print(sch)