def solve():
    N, M = map(int, input().split())
    cnt = bin(N).count('1')
    if M < cnt or (N - M) % 2 != 0:
        print("NO")
    else:
        print("YES")

solve()