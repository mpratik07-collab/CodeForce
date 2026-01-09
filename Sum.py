n=int(input())
l=[]
for i in range(n):
    a,b,c=map(int,input().split())
    if a+b==c or a+c==b or b+c==a:
        l.append("YES")
    else:
        l.append("NO")
for i in l:
    print(i)