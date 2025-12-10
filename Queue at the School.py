n,t=map(int,input().split())
a=list(input())
count=0
for i in range(t):
    j=1
    while j<n:
        if a[j-1]=='B' and a[j]=='G':
            a[j-1],a[j]=a[j],a[j-1]
            j+=1
        j+=1

p=''
for i in a:
    p+=i    
print(p)
