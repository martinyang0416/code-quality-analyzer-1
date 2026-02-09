t = int(input())
for _ in range(t):
    n = int(input())
    names = [input().strip() for _ in range(n)]
    indexed_names = [(name, idx) for idx, name in enumerate(names)]
    sorted_names = sorted(indexed_names, key=lambda x: (x[0].split()[-1].lower(), -x[1]))
    for name, _ in sorted_names:
        print(name)