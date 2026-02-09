def generate_partitions():
    nums = [1, 2, 3, 4, 5, 6]
    partitions = []

    def helper(remaining, path):
        if not remaining:
            partitions.append(path.copy())
            return
        first = remaining[0]
        for i in range(1, len(remaining)):
            pair = (first, remaining[i])
            new_remaining = remaining[1:i] + remaining[i+1:]
            helper(new_remaining, path + [pair])

    helper(nums, [])
    return partitions

all_partitions = generate_partiti