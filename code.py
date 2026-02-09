def minimal_distance(a, b):
    return min(abs(ord(a) - ord(b)), 26 - abs(ord(a) - ord(b)))

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    P = int(input[ptr]); ptr +=1
    Q = int(input[ptr]); ptr +=1
    L = int(input[ptr]); ptr +=1
    U = input[ptr]; ptr +=1
    V = input[ptr]; ptr +=1
    
    windows = []
    for i in range(Q - P + 1):
        cost = 0
        changes = {}
        valid = True
        for k in range(P):
            u_char = U[k]
           