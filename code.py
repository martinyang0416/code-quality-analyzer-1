n = int(input())
a, b = map(int, input().split())
c = int(input())
toppings = [int(input()) for _ in range(n)]
toppings.sort(reverse=True)

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + toppings[i - 1]

max_ratio = c / a  # k=0 case

for k in range(1, n + 1):
    total_cal = c + prefix[k]
    price = a + k * b
    current_ratio = total_cal / price
    if current_ratio > max_ratio:
        max_ratio = current_ratio

print(int(max_ratio))