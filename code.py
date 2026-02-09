import sys

MOD = 10**9 + 7

class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)
    
    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

def main():
    n, q = map(int, sys.stdin.readline().split())
    a = lis