import bisect
t=int(input())
p=[]
for i in range(t):
    n,a=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    left_count = bisect.bisect_left(l, a)
    right_idx = bisect.bisect_right(l, a)
    right_count = n - right_idx
    if left_count >= right_count:
        p.append(a - 1)
    else:
        p.append(a + 1)

for j in p:
    print(j)