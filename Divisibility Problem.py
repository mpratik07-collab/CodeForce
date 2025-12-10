n=int(input())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    if a%b==0:
        l.append(0)
    else:
        l.append(b-(a%b))

for i in l:
    print(i)