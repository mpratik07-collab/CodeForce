
t=int(input())
 
for i in range(t):
    n=int(input())
    a=sorted(set(map(int,input().split())))
    
    ans=0
    c=0
    l=-2000000000 
    
    for x in a:
        if x==l+1:
            c+=1
        else:
            c=1
        
        if c>ans:
            ans=c
        
        l=x
        
    print(ans)