c=input()
u=0
l=0
for i in c:
    if i.isupper():
        u+=1
    else:
        l+=1

if u>l:
    print(c.upper())
else:
    print(c.lower())