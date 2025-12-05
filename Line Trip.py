t = int(input())
l=[]

for i in range(t):
   
    line1 = input().split()
    n = int(line1[0])
    x = int(line1[1])


    line2 = input().split()
    a = []
    for val in line2:
        a.append(int(val))

    min_tank = a[0]


    for i in range(1, n):
        gap = a[i] - a[i-1]
      
        if gap > min_tank:
            min_tank = gap


    last_gap = 2 * (x - a[n-1])
    
    if last_gap > min_tank:
        min_tank = last_gap

    l.append(min_tank)

for val in l:
    print(val)
