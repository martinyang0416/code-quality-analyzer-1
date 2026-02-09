a = int(input())
binary = format(a, '06b')
output = ['0'] * 6

for i in range(6):
    bit = binary[i]
    p = 6 - i  # original position (1-based)
    if p == 1:
        q = 5
    elif p == 2:
        q = 2
    elif p == 3:
        q = 4
    elif p == 4:
        q = 3
    elif p == 5:
        q = 1
    else:  # p == 6
        q = 6
    new_index = 6 - q  # because output_str index for position q is (6 - q)
    output[new_index] = bit

result = int(''.join(output), 2)
print(result)