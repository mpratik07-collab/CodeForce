s=input()
l=[]
for char in s:
    l.append(char)

s=list(set(l))
if len(s)%2==0:
    print("CHAT WITH HER!") 

else:
    print("IGNORE HIM!")    
