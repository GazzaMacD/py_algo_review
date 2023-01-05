"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
    0 <= k <= nums.length


"""
from typing import List


def longest_ones(nums: List[int], k: int) -> int:
    if len(nums) == 0:
        return 0
    else:
        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1
        return right - left + 1


if __name__ == "__main__":
    nums1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k1 = 2
    expected1 = 6
    answer1 = longest_ones(nums1, k1)
    assert answer1 == expected1, f"answer does not equal {expected1}, got {answer1}"

    nums2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k2 = 3
    expected2 = 10
    answer2 = longest_ones(nums2, k2)
    assert answer2 == expected2, f"answer does not equal {expected2}, got {answer2}"

    # check 0 length array
    answer3 = longest_ones([], 1)
