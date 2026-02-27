input()
counts=[0]*5
for x in input().split():
    counts[int(x)]+=1
tax=counts[4]+counts[3]+counts[2]//2
counts[1]=max(0,counts[1]-counts[3])
counts[2]%=2

if counts[2]>0:
    tax+=1
    counts[1]=max(0,counts[1]-2)
if counts[1]>0:
    tax+=(counts[1]+3)//4

print(tax)

