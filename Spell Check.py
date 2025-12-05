c=int(input())
l=[]
for i in range(c):
    n=int(input())
    s=input()
    if len(s)==n:
        if sorted(s) == sorted("Timur"):
            l.append("YES")
        else:
            l.append("NO")
        
    else:
        l.append("NO")
for val in l:
    print(val)