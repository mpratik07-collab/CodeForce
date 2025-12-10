n=int(input())
p="I hate"
if n==1:
 print(p+" it")

else:
    for i in range(2,n+1):
        if i%2==0:
           p+=" that I love "
        else:
           p+=" that I hate "
    print(p+" it")