n=int(input())
l=[]
d=[]
for i in range(n):
    s,p=input().split()
    t=s[0]
    k=p[0]
    s=k+s[1:]
    p=t+p[1:]
    l.append(s)
    d.append(p)

for i in range(n):
    print(l[i],d[i])