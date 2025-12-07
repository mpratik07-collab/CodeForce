n=int(input())
line1=input().split()
line2=input().split()
s=[n*(n+1)]/2
line1=list(set(line1))
line2=list(set(line2))
for val in line1:
    s-=int(val)

for val in line2:
    s-=int(val)

if s==0:
    print("I become the guy.")

else:
    print("Oh, my keyboard!")