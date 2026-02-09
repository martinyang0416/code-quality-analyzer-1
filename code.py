def find_poisoned_duration(time_series, duration):
    if not time_series:
        return 0
    total = 0
    start = time_series[0]
    end = start + duration - 1
    for t in time_series[1:]:
        current_end = t + duration - 1
        if t > end:
            total += end - start + 1
            start = t
            end = current_end
        else:
            end = max(end, current_end)
    total += end - start + 1
    return total