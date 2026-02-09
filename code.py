m = int(input())
h = list(map(int, input().split()))
h.sort()
result = [h[i-1] for i in range(1, len(h))]
print(' '.join(map(str, result)))