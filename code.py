import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        R = int(sys.stdin.readline())
        R_sq = R * R
        points = []
        for _ in range(3):
            x, y = map(int, sys.stdin.readline().split())
            points.append((x, y))
        # Compute pairwise squared distances
        a, b, c = points
        d_ab = (a[0] - b[0])**2 + (a[1] - b[1])**2
        d_ac = (a[0] - c[0])**2 + (a[1] - c[1])**2
        d_bc = (b[0] - c[0])**2 + (b[1] - c[1])**