import sys

def main():
    A, B, T = map(int, sys.stdin.readline().split())
    X = list(map(int, sys.stdin.readline().split())) if A > 0 else []
    Y = list(map(int, sys.stdin.readline().split())) if B > 0 else []
    W = []
    S = []
    for _ in range(T):
        wi, si = map(int, sys.stdin.readline().split())
        W.append(wi)
        S.append(si)
    
    # Compute X_max and Y_max
    X_max = max(X) if A > 0 else 0
    Y_max = max(Y) if B > 0 else 0
    
    problematic = 0
    S_imp 