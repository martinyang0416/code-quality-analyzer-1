n, k = map(int, input().split())

count_div3 = n // 3

if k <= count_div3:
    print(3 * k)
else:
    m = k - count_div3
    # Calculate the m-th non-divisible number
    g = (m - 1) // 2
    r = (m - 1) % 2 + 1
    x = 3 * g + r
    print(x)