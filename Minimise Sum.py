n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    if a==1:
        print(l[0])
    else:
        print(min(2*l[0],l[0]+l[1]))