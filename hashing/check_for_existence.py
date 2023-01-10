"""
Hash tables require O(1) to check for existence. Array's need 0(n) so 
using a hash makes it significantly faster.
"""

"""
1. Two Sum: Given an array of integers nums and an integer target, 
return indices of two numbers such that they add up to target. You 
cannot use the same index twice.
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in dic:  # This operation is O(1)!
            return [i, dic[complement]]
        # add num as key and list index as value
        dic[num] = i

    return [-1, -1]
