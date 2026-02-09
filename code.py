n = int(input())
result = []
for _ in range(n):
    a, b, c, d, e = map(int, input().split())
    
    # Convert each number to a 2-bit binary string
    def to_bits(x, max_val):
        if max_val == 2:
            return f"{x:02b}"
        else:  # max_val is 3
            return f"{x:02b}"
    
    bits = []
    bits.append(to_bits(a, 2))
    bits.append(to_bits(b, 2))
    bits.append(to_bits(c, 2))
    bits.append(to_bits(d, 3))
    bits.append(to_bits(e, 3))
    
    bin_str = ''.join(bits)