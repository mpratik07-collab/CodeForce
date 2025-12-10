l1=input()
l2=input()
r=''
for i in range(len(l1)):
    if l1[i]==l2[i]:
        r=r+'0'

    else:
        r=r+'1'  

print(r)