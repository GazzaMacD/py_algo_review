"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Example 1:

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2

Example 2:

Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive. 

Example 3:

Input: nums = [1,-2,-3]
Output: 5

Constraints:

    1 <= nums.length <= 100
    -100 <= nums[i] <= 100
"""
from typing import List


def min_start_value(nums: List[int]) -> int:
    min_val = curr = 1
    if nums[0] < min_val:
        curr = min_val - nums[0]
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        val = nums[i] + prefix[-1]
        if val > min_val:
            pass
        else:
            curr = max(curr, (min_val - val))
        prefix.append(nums[i] + prefix[-1])
    return curr


if __name__ == "__main__":
    # Example 1:
    nums = [-3, 2, -3, 4, 2]
    ans = 5
    res = min_start_value(nums)
    assert res == ans, f"func running_sum expected {ans}, got {res}"

    # Example 2:
    nums = [1, 2]
    ans = 1
    res = min_start_value(nums)
    assert res == ans, f"func running_sum expected {ans}, got {res}"

    # Example 3:
    nums = [1, -2, -3]
    ans = 5
    res = min_start_value(nums)
    assert res == ans, f"func running_sum expected {ans}, got {res}"

    # Example 4:
    nums = [-3, 6, 2, 5, 8, 6]
    ans = 4
    res = min_start_value(nums)
    assert res == ans, f"func running_sum expected {ans}, got {res}"
    print("Success!!")
