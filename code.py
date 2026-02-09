def calculate_total_segments(x, y):
    segment_map = {
        '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
        '5': 5, '6': 6, '7': 3, '8': 7, '9': 6,
        '-': 4
    }
    
    total = 0
    for number in range(x, y + 1):
        s = str(number)
        for c in s:
            total += segment_map[c]
        if number != y:
            total += segment_map['-']
    
    return total

x, y = map(int, input().split())
print(calculate_total_segments(x, y))