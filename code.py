def main():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    k = int(input[1])
    m = int(input[2])  # Note: m is read but not used in this approach
    cities = list(map(int, input[3:3+n]))
    
    # Create runs
    runs = []
    if not cities:
        print(0)
        return
    current_city = cities[0]
    current_count = 1
    for city in cities[1:]:
        if city == current_city:
            current_count += 1
        else:
            runs.append((current_c