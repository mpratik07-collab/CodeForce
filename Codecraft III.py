months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
s = input()
k = int(input())
idx = months.index(s)
print(months[(idx + k) % 12])