import math

T = int(input())
for _ in range(T):
    n = int(input())
    m = 2 * n
    angle = math.pi / (2 * m)
    result = 1.0 / (2 * math.sin(angle))
    print("{0:.9f}".format(result))