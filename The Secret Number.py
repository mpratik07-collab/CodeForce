import sys
input_data = sys.stdin.read().split()

if input_data:
    iterator = iter(input_data)
    t = int(next(iterator))

    for _ in range(t):
        n = int(next(iterator))
        ans = []

        
        for k in range(1, 19):
            denominator = 10**k + 1
            
            if denominator > n:
                break
          
            if n % denominator == 0:
                ans.append(n // denominator)

        # The problem requires the output in ascending order
        ans.sort()
        
        # Print count followed by the values
        print(len(ans), *ans)