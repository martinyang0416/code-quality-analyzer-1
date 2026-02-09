n = input().strip()
print(1 if any(c in {'2','3','5','7'} for c in n) else 0)