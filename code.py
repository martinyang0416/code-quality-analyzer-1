def main():
    import sys
    s = sys.stdin.readline().strip()
    n = len(s)
    B = [0] * (n + 1)
    E = [0] * (n + 1)
    S = [0] * (n + 1)
    I = [0] * (n + 1)

    for i in range(n):
        B[i+1] = B[i] + (1 if s[i] == 'b' else 0)
        E[i+1] = E[i] + (1 if s[i] == 'e' else 0)
        S[i+1] = S[i] + (1 if s[i] == 's' else 0)
        I[i+1] = I[i] + (1 if s[i] == 'i' else 0)
    
    total = 0

    for r in range(1, n+1):
        stack = []
        current_min = float('inf')
       