n=int(input())
k=1
while True:
    t=k*(k+1)//2
    if n==t:
        break
    if n<t:
        break
    k+=1

if n==t:
    print("YES")

else:
    print("NO")
