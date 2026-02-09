def main():
    import sys
    s = sys.stdin.readline().strip()
    N = len(s)
    T = ['b', 'e', 's', 's', 'i', 'e']  # The target "bessie" characters

    count = [0] * 7
    count[0] = 1  # base case: 1 way to form 0 characters
    sum_s = [0] * 7  # sum_s[0] is 0 since start is undefined for empty subsequence
    total = 0

    for pos in range(N):
        c = s[pos]
        prev_count = count.copy()
        prev_sum = sum_s.copy()

        # Update the count and sum_s arrays for each possib