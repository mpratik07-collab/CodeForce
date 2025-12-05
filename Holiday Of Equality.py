n = int(input())
l2 = list(map(int, input().split()))

max1 = max(l2)

count = 0
for i in l2:
    count += max1 - i

print(count)