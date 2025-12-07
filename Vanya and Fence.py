line1 = input().split()
n = int(line1[0])
h = int(line1[1])
line2 = input().split()
c=0
for val in line2:
    a=int(val)
    if a<=h:
        c+=1
    else:
        c+=2

print(c)