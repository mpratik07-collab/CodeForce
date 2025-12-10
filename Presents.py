n=int(input())
l=list(map(int,input().split()))
p=[0]*n
for i in range(n):
    c=l[i]-1    
    p[c]=i+1

for j in p:
    print(j,end=' ')
