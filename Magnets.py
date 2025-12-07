n=int(input())
l=[]
for i in range(n):
    m=int(input())
    l.append(m)
grp=1
for i in range(1,n):
    if l[i]!=l[i-1]:
        grp+=1

print(grp)