import sys

def main():
    T_target = ['b', 'e', 's', 's', 'i', 'e']
    
    # Read input
    s = sys.stdin.readline().strip()
    n = len(s)
    matrices = []
    for c in s:
        mat = [[0]*7 for _ in range(7)]
        mat[0][0] = 1
        for i in range(1, 7):
            mat[i][i] = 1
            if c == T_target[i-1]:
                mat[i][i-1] = 1
        matrices.append(mat)
    
    # Compute initial V array
    D0 = [0]*7
    D0[0] = 1
    V = []
    current = [0]*7  # Initial st