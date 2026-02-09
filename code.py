S = input().strip()

balance_low = 0
balance_high = 0
global_min = 0
global_max = 0

for c in S:
    if c == '0':
        new_low = balance_low + 1
        new_high = balance_high + 1
        new_gmin = min(global_min, new_low)
        new_gmax = max(global_max, new_high)
        balance_low, balance_high = new_low, new_high
        global_min, global_max = new_gmin, new_gmax
    elif c == '1':
        new_low = balance_low - 1
        new_high = balance_high - 1
        new_gmin = min(global_mi