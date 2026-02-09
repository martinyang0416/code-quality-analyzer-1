def determine_winner():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        total = sum(a)
        
        if n == 1:
            results.append("ALICE")
            continue
        
        # Compute max prefix sum (exclude entire array)
    