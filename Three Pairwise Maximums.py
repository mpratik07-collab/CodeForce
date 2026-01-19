import sys

input = sys.stdin.read
data = input().split()

iterator = iter(data)

t_str = next(iterator)
if t_str:
    t = int(t_str)
    
    for _ in range(t):
        x = int(next(iterator))
        y = int(next(iterator))
        z = int(next(iterator))
        
        a = [x, y, z]
        a.sort()
        if a[1] != a[2]:
            print("NO")
        else:
            print("YES")

            print(f"{a[0]} {a[0]} {a[2]}")