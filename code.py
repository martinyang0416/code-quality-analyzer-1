k, d, t = map(int, input().split())

m = (k + d - 1) // d
cycle_len = m * d
on_time = k
off_time = cycle_len - on_time
progress_per_cycle = 2 * on_time + off_time
total_progress_needed = 2 * t

full_cycles = total_progress_needed // progress_per_cycle
remainder = total_progress_needed % progress_per_cycle

if remainder == 0:
    total_time = full_cycles * cycle_len
else:
    if remainder <= 2 * on_time:
        time_add = remainder / 2.0
    else:
        time_add = on_time + (remainder - 2 * on