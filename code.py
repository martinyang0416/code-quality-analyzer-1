n = int(input())
a = list(map(int, input().split()))
targets = []
row_usage = {}  # Track the number of targets per row
col_usage = {}  # Track the number of targets per column

# For the given a_i values, we need to construct the targets
# We'll process each column from left to right (0 to n-1)

for i in range(n):
    ai = a[i]
    if ai == 0:
        continue
    elif ai == 1:
        # Find a row where this column can be placed without any target to the east in the same row
        # Use row 