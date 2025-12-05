line1 = input().split()
n = int(line1[0])
k = int(line1[1])


line2 = input().split()


valid_students = 0

for val in line2:
    
    past_participation = int(val)
    
    if past_participation + k <= 5:
        valid_students = valid_students + 1


teams = valid_students // 3

print(teams)