line = input().split()
a = int(line[0])
b = int(line[1])

years = 0

while a <= b:
    a = a * 3
    b = b * 2
    years = years + 1

print(years)