cnt1, cnt2, x, y = map(int, input().split())
lcm = x * y  # Since x and y are distinct primes

low = 1
high = 10**18

while low < high:
    mid = (low + high) // 2
    a = mid - mid // x
    b = mid - mid // y
    c = mid - mid // lcm
    
    if a >= cnt1 and b >= cnt2 and c >= (cnt1 + cnt2):
        high = mid
    else:
        low = mid + 1

print(low)