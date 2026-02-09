def findMinMoves(machines):
    n = len(machines)
    total = sum(machines)
    if total % n != 0:
        return -1
    target = total // n
    surplus = [m - target for m in machines]
    max_surplus = max(surplus)
    cum_sum = 0
    max_cum = 0
    for s in surplus:
        cum_sum += s
        current_abs = abs(cum_sum)
        if current_abs > max_cum:
            max_cum = current_abs
    return max(max_surplus, max_cum)