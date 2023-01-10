"""
3: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""
from typing import List


def running_sum(nums: List[int]) -> List[int]:
    if len(nums) == 0:
        return []
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    return prefix


if __name__ == "__main__":
    # Example 1:
    nums = [1, 2, 3, 4]
    ans = [1, 3, 6, 10]
    res = running_sum(nums)
    assert res == ans, f"func running_sum expected {ans}, got {res}"

    # Example 2:
    nums = [1, 1, 1, 1, 1]
    ans = [1, 2, 3, 4, 5]
    res = running_sum(nums)
    assert res == ans, f"func running_sum expected {ans}, got {res}"

    # Example 3:
    nums = [3, 1, 2, 10, 1]
    ans = [3, 4, 6, 16, 17]
    res = running_sum(nums)
    assert res == ans, f"func running_sum expected {ans}, got {res}"

    print("Success!!")
