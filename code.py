import math

def convex_hull(points):
    points = sorted(points)
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2:
            x1, y1 = lower[-2]
            x2, y2 = lower[-1]
            x3, y3 = p
            cross_val = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
            if cross_val <= 0:
                lower.pop()
            else:
                break
        lower.append(p)
    upper = []
    for p in reversed(point