import collections

def longestPrefix(nums):
    current_freq = collections.defaultdict(int)
    freq_freq = collections.defaultdict(int)
    max_length = 0

    for i, num in enumerate(nums):
        old_count = current_freq[num]
        if old_count > 0:
            freq_freq[old_count] -= 1
            if freq_freq[old_count] == 0:
                del freq_freq[old_count]
        current_freq[num] += 1
        new_count = current_freq[num]
        freq_freq[new_count] += 1

        if len(fre