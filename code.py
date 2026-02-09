m, n = map(int, input().split())
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

# Flip rows where the first element is 0
for i in range(m):
    if matrix[i][0] == 0:
        for j in range(n):
            matrix[i][j] ^= 1

# Check each column (from 1 to n-1) and flip if needed
for j in range(1, n):
    cnt = sum(matrix[i][j] for i in range(m))
    if cnt < m - cnt:
        for i in range(m):
            matrix[i][j] ^= 1

# Calculate the total s