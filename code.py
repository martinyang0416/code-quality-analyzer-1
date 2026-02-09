h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

if h == 0:
    print(0)
    exit()

prev_row = grid[0]

for i in range(1, h):
    current_row = []
    for j in range(w):
        max_prev = 0
        # Check possible positions from the previous row
        for k in [j-1, j, j+1]:
            if 0 <= k < w:
                if prev_row[k] > max_prev:
                    max_prev = prev_row[k]
        current_row.append(max_prev + grid[i][j])
    prev_row