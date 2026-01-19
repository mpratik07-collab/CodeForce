n = int(input())
l = list(map(int, input().split()))
f = l.count(-1) 
c = 0            
d = 0           

for i in l:
    if i > 0:
        d += i
    else:
        if d > 0:
            c += 1
            d -= 1 

print(f - c)