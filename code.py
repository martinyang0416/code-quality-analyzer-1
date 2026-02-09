import sys

def generate_pairings(numbers):
    if not numbers:
        return [[]]
    first = numbers[0]
    result = []
    for i in range(1, len(numbers)):
        pair = (first, numbers[i])
        remaining = numbers[1:i] + numbers[i+1:]
        for p in generate_pairings(remaining):
            result.append([pair] + p)
    return result

all_numbers = [1, 2, 3, 4, 5, 6]
all_pairings = generate_pairings(all_numbers)

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
   