t=int(input())
for i in range(t):
    s=int(input())
    l=list(map(int,input().split()))
    c=max(l)
    print(s*c)