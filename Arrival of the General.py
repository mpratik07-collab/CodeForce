n = int(input())

a = list(map(int, input().split()))

max_height = max(a)
max_index = a.index(max_height)

min_height = min(a)
min_index = 0

for i in range(n):
    if a[i] == min_height:
        min_index = i

moves_max = max_index

moves_min = (n - 1) - min_index

total_seconds = moves_max + moves_min

if max_index > min_index:
    total_seconds -= 1

print(total_seconds)