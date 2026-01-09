n=int(input())
l=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)

t=0
for j in range(n):
    for k in range(j+1,n):
        if l[j][0] == l[k][1]:
            t+=1
        if l[j][1] == l[k][0]:
            t+=1

print(t)
