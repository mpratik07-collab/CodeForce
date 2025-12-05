t=int(input())
l=[]
c=0
d=['c','o','d','e','f','o','r','c','e','s']
for i in range(t):
    s=input()
    for j in range (len(d)):
        if d[j]!=s[j]:
            c+=1
    
    l.append(c)
    c=0

for val in l:
    print(val)