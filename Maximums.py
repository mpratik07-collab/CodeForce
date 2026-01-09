n=int(input())
l=list(map(int,input().split()))
c=[]
cmax=0
for b in l:
    a=b+cmax
    c.append(a)
    cmax=max(cmax,a)

print(*(c))