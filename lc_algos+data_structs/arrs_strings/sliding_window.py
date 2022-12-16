from typing import List

"""
Example 1: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.
"""


def find_longest_subarray(list_nums: List[int], constraint: int) -> int:
    """Takes array of positive integers nums and an integer k, finds the length of the longest subarray whose sum is less than or equal to k.
    Time complexity: O(n)
    Space complexity: 0(1)
    """
    left = sum_curr_window = longest = 0
    for right in range(len(list_nums)):
        sum_curr_window += list_nums[right]
        while sum_curr_window > constraint:
            # shrink window from left
            sum_curr_window -= list_nums[left]
            left += 1
        longest = max(longest, right - left + 1)

    return longest


if __name__ == "__main__":
    arr1 = [3, 1, 2, 7, 4, 2, 1, 1, 5]
    lim1 = 8
    print(find_longest_subarray(arr1, lim1))
