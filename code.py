import sys

def compute_max(arr, k):
    max_p = -float('inf')
    n = len(arr)
    for i in range(n - k + 1):
        product = 1
        for j in range(i, i + k):
            product *= arr[j]
        if product > max_p:
            max_p = product
    return max_p

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    if len(parts) < 2:
        continue
    n, k = map(int, parts)
    if n == 0 and k == 0:
        break
    cards = []
   