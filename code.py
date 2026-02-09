def is_monotonic(s):
    n = len(s)
    if n <= 1:
        return True
    increasing = True
    decreasing = True
    for i in range(n - 1):
        if s[i] > s[i+1]:
            increasing = False
        if s[i] < s[i+1]:
            decreasing = False
    return increasing or decreasing

def main():
    s = input().strip()
    for i in range(1, len(s)):
        part1 = s[:i]
        part2 = s[i:]
        if is_monotonic(part1) and is_monotonic(part2):
            print("YES")
            ret