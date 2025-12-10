a=list(map(int,input().split()))
b=max(a)
l=[]
for i in a:
    if i!=b:
        l.append(b-i)

for i in l:     
    print(i,end=' ')    