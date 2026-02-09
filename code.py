t = int(input())
for _ in range(t):
    m = int(input())
    b = list(map(int, input().split()))
    b.sort(reverse=True)
    mia = 0
    friend = 0
    for i in range(m):
        if i % 2 == 0:
            mia += b[i]
        else:
            friend += b[i]
    if mia > friend:
        print("WIN")
    elif mia < friend:
        print("LOSE")
    else:
        print("DRAW")