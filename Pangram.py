n=int(input())
l=input()
l=l.lower()
if n<26:
    print("NO")

else:
    c=list(l)
    c=list(set(c))
    if len(c)<26:
        print("NO") 

    else:
        print("YES")
