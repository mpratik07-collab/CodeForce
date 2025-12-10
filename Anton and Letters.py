s = input()

dl = set()
for char in s:
    if 'a' <= char <= 'z':
        dl.add(char)

print(len(dl))