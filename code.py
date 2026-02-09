s = input().strip()

args = []
current_arg = []
state = 'outside'

for char in s:
    if state == 'outside':
        if char == ' ':
            if current_arg:
                args.append(''.join(current_arg))
                current_arg = []
        elif char == '[':
            if current_arg:
                args.append(''.join(current_arg))
                current_arg = []
            state = 'inside'
        else:
            current_arg.append(char)
    else:
        if char == ']':
     