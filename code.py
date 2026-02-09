import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    A = int(input[idx]); idx +=1
    B = int(input[idx]); idx +=1
    T = int(input[idx]); idx +=1

    X = []
    if A > 0:
        X = list(map(int, input[idx:idx+A]))
        idx += A
    Y = []
    if B > 0:
        Y = list(map(int, input[idx:idx+B]))
        idx += B

    W = []
    S = []
    for _ in range(T):
        w = int(input[idx]); idx +=1
        s = int(input[idx]); idx +=1
        W.appen