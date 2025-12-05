X=int(input())
C=0
for i in range(X):
    Y=input()
    if Y=="X++" or Y=="++X":
        C+=1

    if Y=="X--" or Y=="--X":
        C-=1

print(C)