from collections import Counter

def originalDigits(s):
    freq = Counter(s)
    digits = [0] * 10
    processing_order = [
        (0, 'z', ['z', 'e', 'r', 'o']),
        (2, 'w', ['t', 'w', 'o']),
        (4, 'u', ['f', 'o', 'u', 'r']),
        (6, 'x', ['s', 'i', 'x']),
        (8, 'g', ['e', 'i', 'g', 'h', 't']),
        (3, 'h', ['t', 'h', 'r', 'e', 'e']),
        (5, 'f', ['f', 'i', 'v', 'e']),
        (7, 's', ['s', 'e', 'v', 'e', 'n']),
        (1, 'o', ['o', 'n', 'e']),
        (9, 'i'