ax, ay, bx, by, cx, cy = map(int, input().split())

# Coefficients for perpendicular bisectors of AB and BC
A1 = 2 * (bx - ax)
B1 = 2 * (by - ay)
C1 = (ax**2 + ay**2) - (bx**2 + by**2)

A2 = 2 * (cx - bx)
B2 = 2 * (cy - by)
C2 = (bx**2 + by**2) - (cx**2 + cy**2)

# Calculate determinant for line intersection
D = A1 * B2 - A2 * B1

if D != 0:
    # Calculate intersection point O
    x = (B1 * C2 - B2 * C1) / D
    y = (A2 * C1 - A1 * C2) / D

    # Vectors from O to A, B, C
    oax = ax - x
    o