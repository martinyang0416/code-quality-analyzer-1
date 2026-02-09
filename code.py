import sys

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        a, b = map(int, line.strip().split())
        if a == 0 and b == 0:
            break
        
        groupA = []
        for _ in range(a):
            x = int(sys.stdin.readline())
            groupA.append(x)
        
        groupB = []
        for _ in range(b):
            y = int(sys.stdin.readline())
            groupB.append(y)
        
        sumA = sum(groupA)
 