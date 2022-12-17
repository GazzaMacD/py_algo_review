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


"""
2: You are given a binary substring s (a string containing only "0" and "1"). An operation involves flipping a "0" into a "1". What is the length of the longest substring containing only "1" after performing at most one operation?

For example, given s = "1101100111", the answer is 5. If you perform the operation at index 2, the string becomes 1111100111.

"""


def find_longest_ones(s: str) -> int:
    """
    Given max one operation involves flipping a "0" into a "1", what is the length of the longest substring containing only "1"?

    For example, given s = "1101100111", the answer is 5. If you perform the operation at index 2, the string becomes 1111100111.
    """
    left = current = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            current += 1
        while current > 1:
            if s[left] == "0":
                current -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans


if __name__ == "__main__":
    arr1 = [3, 1, 2, 7, 4, 2, 1, 1, 5]
    lim1 = 8
    print(find_longest_subarray(arr1, lim1))
