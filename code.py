def main():
    import sys

    # Read the first line: x, y, z
    x, y, z = map(int, sys.stdin.readline().split())
    
    # Read the number of monitors
    n = int(sys.stdin.readline())
    
    # Read each monitor's cost and type
    hdmi = []
    vga = []
    for _ in range(n):
        parts = sys.stdin.readline().split()
        cost = int(parts[0])
        typ = parts[1]
        if typ == 'HDMI':
            hdmi.append(cost)
        else:
            vga.append(cost)
    
    # Sort the 