import sys
import math
input=sys.stdin.read().split()

iterator=iter(input)
try:
    t=int(next(iterator))
except StopIteration:
    t=0

for i in range(t):
    l=int(next(iterator))
    a=int(next(iterator))
    b=int(next(iterator))
    if l<b:
        print(0)


    else:
        g=math.gcd(b,l)
        