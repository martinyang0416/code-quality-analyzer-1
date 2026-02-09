def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    elements = []
    sum_stored = 0
    offset = 0
    for _ in range(n):
        ti = int(input[ptr])
        if ti == 1:
            x = int(input[ptr+1])
            ptr +=2
            stored = x - offset
            elements.append(stored)
            sum_stored += stored
        elif ti == 2:
            ptr +=1
            if elements:
                e = elements.pop()
      