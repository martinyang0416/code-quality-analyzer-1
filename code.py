import sys

def main():
    input = sys.stdin.read().split()
    s = list(input[0])
    U = int(input[1])
    updates = []
    pos = 2
    for _ in range(U):
        p = int(input[pos]) - 1  # convert to 0-based index
        c = input[pos+1]
        updates.append((p, c))
        pos += 2

    n = len(s)
    T = ['b', 'e', 's', 's', 'i', 'e']

    def compute_total_and_prefix(s):
        n = len(s)
        current = [0] * 6
        current[0] = 1
        total = []
        for char in s:
      