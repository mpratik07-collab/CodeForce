line = input().split()
Y = int(line[0])
W = int(line[1])

if Y > W:
    max_score = Y
else:
    max_score = W

winning_counts = 6 - max_score + 1

if winning_counts == 1:
    print("1/6")
elif winning_counts == 2:
    print("1/3")
elif winning_counts == 3:
    
    print("1/2")
elif winning_counts == 4:
   
    print("2/3")
elif winning_counts == 5:
    print("5/6")
elif winning_counts == 6:
   
    print("1/1")
else:
    print("0/1")