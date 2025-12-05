X=int(input())
problems_solved=0

for i in range(X):
    Y=list(map(int,input().split()))
    count=sum(Y)
    if count>=2:
        problems_solved+=1

print(problems_solved)