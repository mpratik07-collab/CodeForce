n = int(input())

p = list(map(int, input().split()))

result = sum(p) / n

print(f"{result:.12f}")