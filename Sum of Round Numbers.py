t = int(input())

for j in range(t):
    number_str = input()
    length = len(number_str)
    res = []
    
    for i in range(length):
        if number_str[i] != '0':                                                                                                            
            zeros = '0' * (length - 1 - i)
            res.append(number_str[i] + zeros)
            
  
    print(len(res))
   
    print(*(res))