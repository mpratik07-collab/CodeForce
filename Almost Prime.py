n = int(input())
factor_count = [0] * (n + 1)

for i in range(2, n + 1):
    if factor_count[i] == 0:
        for multiple in range(i, n + 1, i):
            factor_count[multiple] += 1

result = 0
for count in factor_count:
    if count == 2:
        result += 1
print(result)