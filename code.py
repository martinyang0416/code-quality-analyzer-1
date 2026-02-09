import math
from functools import reduce

def is_good_array(nums):
    return reduce(math.gcd, nums) == 1