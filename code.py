def find_min_fibonacci_numbers(k):
    fibs = [1, 1]
    while True:
        next_fib = fibs[-1] + fibs[-2]
        if next_fib > k:
            break
        fibs.append(next_fib)
    count = 0
    for num in reversed(fibs):
        if k >= num:
            count += 1
            k -= num
            if k == 0:
                break
    return count