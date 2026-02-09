import heapq

h, w, n, r = map(int, input().split())

grid = []
start = None
for i in range(h):
    row = list(input().strip())
    for j in range(w):
        if row[j] == '@':
            start = (i, j)
    grid.append(row)

treasures = {}
treasure_values = []
for i in range(n):
    m, v = input().split()
    v = int(v)
    treasures[m] = (i, v)
    treasure_values.append(v)

def get_sum(mask):
    total = 0
    for i in range(n):
        if mask & (1 << i):
            total += treasure_values