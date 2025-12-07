n = int(input())

line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))

levels_x = line1[1:]
levels_y = line2[1:]

all_levels = levels_x + levels_y

unique_levels = set(all_levels)

if len(unique_levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")