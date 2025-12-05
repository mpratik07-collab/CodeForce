n = int(input())
s = input()

removed_count = 0

for i in range(1, n):
    if s[i] == s[i-1]:
        removed_count = removed_count + 1

print(removed_count)