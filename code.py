def rotate90(mat):
    if not mat or not mat[0]:
        return []
    a = len(mat)
    b = len(mat[0])
    rotated = []
    for c in range(b):
        new_row = []
        for r in range(a):
            new_row.append(mat[a - r - 1][c])
        rotated.append(''.join(new_row))
    return rotated

def rotate270(mat):
    if not mat or not mat[0]:
        return []
    r1 = rotate90(mat)
    r2 = rotate90(r1)
    r3 = rotate90(r2)
    return r3

def find_unique_divisions(grid, N, M):
    divisors