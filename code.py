import bisect

def compute_makespan(toys_values, robots_capacities):
    counts = [0] * len(robots_capacities)
    for val in toys_values:
        idx = bisect.bisect_right(robots_capacities, val) - 1
        if idx < 0:
            return float('inf')  # Should not happen if initial checks passed
        counts[idx] += 1
    return max(counts) if counts else 0

def putaway(A, B, T, X, Y, W, S):
    if A == 0 and B == 0:
        return -1  # per problem constraints, but should be checked earlier