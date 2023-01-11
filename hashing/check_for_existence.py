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
    for i, num in enumerate(nums, 0):
        complement = target - num
        if complement in dic:  # This operation is O(1)!
            return [i, dic[complement]]
        # add num as key and list index as value
        dic[num] = i

    return [-1, -1]


print("\n+++++++++ two_sum_index +++++++++++")
print(two_sum_index([1, 2, 5, 2, 8, 9, 10], 12), "expect [6, 3]")
print(two_sum_index([1, 2, 5, 2, 8, 9, 10], 20), "expect [-1, -1]")

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


print("\n+++++++++ two_sum_exists +++++++++++")
print(two_sum_exists([1, 2, 5, 2, 8, 9, 10], 12), "expect True")
print(two_sum_exists([1, 2, 5, 2, 8, 9, 10], 20), "expect False")


"""
3: 2351. First Letter to Appear Twice
Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.
"""


def repeated_char(s: str) -> str:
    """
    Brute force would be O(n) but
    """
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return ""


print("+++++++++ repeated_char +++++++++++")
print(repeated_char("abcdefghichahal"), "expect c")

"""
4: Given an integer array nums, find all the numbers x that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.
"""


def find_nums(nums: List[int]) -> List[int]:
    ans = []
    s = set(nums)
    for num in nums:
        if (num + 1 not in s) and (num - 1 not in s):
            ans.append(num)
    return ans


print("+++++++++ find_nums +++++++++++")
print(find_nums([1, 2, 3, 10]), "expect [10]")
