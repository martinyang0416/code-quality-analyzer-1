import sys
from collections import deque

def precompute_tetra(max_num):
    tetra = []
    n = 1
    while True:
        t = n * (n + 1) * (n + 2) // 6
        if t > max_num:
            break
        tetra.append(t)
        n += 1
    tetra.sort(reverse=True)  # Sort in descending order for efficiency
    return tetra

def precompute_odd_tetra(max_num):
    tetra = []
    n = 1
    while True:
        t = n * (n + 1) * (n + 2) // 6
        if t > max_num:
            break
        if n % 4 ==