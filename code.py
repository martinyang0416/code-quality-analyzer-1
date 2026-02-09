import sys

def main():
    max_n = 10**6
    rsum = [0] * (max_n + 1)
    rsum[0] = 0
    for n in range(1, max_n + 1):
        if n == 1:
            rsum[n] = 1
        elif n == 2:
            rsum[n] = 2
        elif n == 3:
            rsum[n] = 6
        elif n == 4:
            rsum[n] = 6
        elif n == 5:
            rsum[n] = 3
        else:
            rsum[n] = 9
    
    pre_sum = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        pre_sum[i] = pre_sum[i-1] + rsum[i]
   