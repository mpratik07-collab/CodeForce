import sys

input=sys.stdin.read().split()
iterator=iter(input)
try:
    t=int(next(iterator))

except StopIteration:
    t=0

for i in range (t):
    c=int(next(iterator))
    if c%2!=0:
        print(0)
    else:
        print((c//4)+1)