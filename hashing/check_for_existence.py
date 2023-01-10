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


def two_sum_index(nums: List[int], target: int) -> List[int]:
    """
    Use dic to store num as key. Increase from O(n2) --> O()
    """
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in dic:  # This operation is O(1)!
            return [i, dic[complement]]
        # add num as key and list index as value
        dic[num] = i

    return [-1, -1]


"""
2. Two Sum: Given an array of integers nums and an integer target, 
return True if two numbers exist such that they add up to target or false otherwise.  
"""


def two_sum_exists(nums: List[int], target: int) -> bool:
    """
    Use set to store nums
    """
    s = set()
    for num in nums:
        complement = target - num
        if complement in s:  # This operation is O(1)!
            return True
        s.add(num)
    return False


print(" two_sums_exists")
print(two_sum_exists([1, 2, 5, 2, 8, 9, 10], 12), "expect True")
print(two_sum_exists([1, 2, 5, 2, 8, 9, 10], 20), "expect False")
