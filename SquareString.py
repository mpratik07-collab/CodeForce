c=int(input())
l=[]
for i in range(c):
    d=input()
    l.append(d)


for j in l:
    if len(j)%2==0:
        n=int(len(j)/2)
        first_half=j[:n]
        second_half=j[n:]
        if first_half==second_half:
            print("YES")
        else:
            print("NO")

    else:
        print("NO")

        
