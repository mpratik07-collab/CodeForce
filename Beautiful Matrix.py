for r in range(5):
    row = input().split()
    
    if '1' in row:
       
        c = row.index('1')
    
        vertical_moves = abs(r - 2)
        horizontal_moves = abs(c - 2)
        
        print(vertical_moves + horizontal_moves)
        break