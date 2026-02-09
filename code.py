def generate_all_matchings(elements):
    if not elements:
        yield []
        return
    first = elements[0]
    for i in range(1, len(elements)):
        pair = (first, elements[i])
        remaining = elements[1:i] + elements[i+1:]
        for sub_match in generate_all_matchings(remaining):
            yield [pair] + sub_match

# Precompute all possible perfect matchings for 1-6
elements = [1, 2, 3, 4, 5, 6]
all_matchings = list(generate_all_matchings(elements))

def solve():
    import 