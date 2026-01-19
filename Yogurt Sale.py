t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    if n%2==0:
        if 2*a>b:
            print(b*(n//2))

        else:
            print(n*a)

    else:
        if 2*a>b:
            print(((n-1)//2)*(b)+a)

        else:
            print(a*n)
        