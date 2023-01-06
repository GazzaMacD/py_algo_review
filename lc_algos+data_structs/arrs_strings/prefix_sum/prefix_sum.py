from typing import List


def build_prefix_sum(nums: List[int]) -> List[int]:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    return prefix


"""
Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2] and queries = [[0, 3], [2, 5], [2, 4]] and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
"""


def answer_queries(nums: List[int], queries: List[List[int]], limit: int) -> List[bool]:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans


if __name__ == "__main__":

    # Build prefix sum
    nums = [5, 2, 1, 6, 3, 8]
    expected = [5, 7, 8, 14, 17, 25]
    ans = build_prefix_sum(nums)
    assert ans == expected, f"build_prefix_sum did not return {expected}, got {ans}"

    # Example 1
    nums = [1, 6, 3, 2, 7, 2]
    queries = [[0, 3], [2, 5], [2, 4]]
    expected = [True, False, True]
    limit = 13
    ans = answer_queries(nums, queries, limit)
    assert ans == expected, f"answer_queries did not return {expected}, got {ans}"
