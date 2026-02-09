m, b = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()
total = 0
count = 0
for price in prices:
    if total + price <= b:
        total += price
        count += 1
    else:
        break
print(count)