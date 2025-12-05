t=int(input())
l=[]
for i in range(t):
    a,b,c=map(int,input().split())
    if (a==b and a!=c):
        l.append(c)

    elif (a==c and a!=b):
        l.append(b)     

    elif (b==c and b!=a):
        l.append(a)
    
for val in l:
    print(val)