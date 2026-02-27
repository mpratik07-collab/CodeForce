import sys
input=sys.stdin.read().split()

iterator=iter(input)
try:
    t=int(next(iterator))
except StopIteration:
    t=0

for i in range(t):
    n=int(next(iterator))
    k=int(next(iterator))
    counts=[0]*(n+1)
    
    for j in range(n):
        val=int(next(iterator))
        if val<=n:
            counts[val]+=1
            
    mc=0
    for i in range(k):
        if counts[i]==0:
            mc+=1
    count_k=counts[k]
    print(max(mc,count_k))