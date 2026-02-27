import sys
input=sys.stdin.read().split()

iterator=iter(input)

if input:
    t=int(next(iterator))

    for i in range(t):
        n=int(next(iterator))
        
        operations=0
        neg=0
        
        for j in range(n):
            val=int(next(iterator))
            
            if val==0:
                operations+=1
            elif val==-1:
                neg+=1

        if neg%2==1:
            operations+=2
            
        print(operations)