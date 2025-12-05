def prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))

prime1=x+1

while True:
    if prime(prime1):
        break
    prime1+=1

if prime1==y:
    print("YES")
else:
    print("NO")
