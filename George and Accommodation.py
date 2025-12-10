n=int(input())
c=0
for i in range(n):
    line1=input().split()
    a=int(line1[0])
    b=int(line1[1])
    if b-a>=2:
        c+=1

print(c)