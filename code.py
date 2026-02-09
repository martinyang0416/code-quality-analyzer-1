def count_subsequences():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    Q = int(data[1])
    a = list(map(int, data[2:2+N]))
    
    prefix = [0] * (N + 1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + a[i-1]
    
    A = [0] * (N + 1)
    for j in range(N+1):
        A[j] = prefix[j] - j
    
    freq_map = {}
    current_mod = A[0] % Q
    freq_map[current_mod] = 1
    
    result = 0
    
    for j in range(1, N+1):
       