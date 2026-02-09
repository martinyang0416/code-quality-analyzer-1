import heapq

n, m, k = map(int, input().split())
grid = []
start = None
end = None
for i in range(n):
    row = input().strip()
    grid.append(row)
    for j in range(m):
        if row[j] == 'S':
            start = (i, j)
        elif row[j] == 'T':
            end = (i, j)
si, sj = start
ti, tj = end

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

heap = []
heapq.heappush(heap, (0, '', si, sj, 0))
visited = {}

found = False
result = None

while heap:
    dist, path, i, j, bitmask = heapq.heappop(h