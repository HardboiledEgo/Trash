q=list(str(input()).split())

c=int(q[0])
x=int(q[1])
y=int(q[2])
z=int(q[3])
m=int(q[4])
s=int(q[5])
f=int(q[6])
e=int(q[7])
t=int(q[8])
a=0
b=0
time=0

while a<c and b<e:
    time+=m
    a=0
    if s>x:
        if (s-x)%z != 0:
            kol_hran = (s-x)//z+1
        else:
            kol_hran = (s-x)/z
        if x/(kol_hran*y)>=1:
            a=x-kol_hran*y
            x+=kol_hran*z
        else:
            while x/(kol_hran*y)<1:
                kol_hran-=1 
            a=x-kol_hran*y
            x+=kol_hran*z
    else:
        a=x

    b+=a//f
    a-=b*f

if a>=c:
    print(time)
else:
    if b>e:
        print(time+t)