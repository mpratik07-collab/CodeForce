n=int(input())
t=0
maxc=0
for i in range(n):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    t+=b-a
    if t>maxc:
        maxc=t
    

print(maxc)