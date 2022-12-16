from typing import List

"""
6: Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""


def sorted_squares(nums: List[int]) -> List[int]:
    """Squares numbers in list and returns a new list with numbers in non-decreasing order

    Time complexity 0(n)
    Space complexity 0(1)
    """
    end = len(nums) - 1
    left, right = 0, end
    # make copy of nums array
    sorted_squares = nums[:]
    for i in range(end, -1, -1):
        if abs(nums[right]) > abs(nums[left]):
            sorted_squares[i] = nums[right] ** 2
            right -= 1
        else:
            sorted_squares[i] = nums[left] ** 2
            left += 1
    return sorted_squares


def main():
    nums = [-4, -1, 0, 3, 10]
    print(sorted_squares(nums))


if __name__ == "__main__":
    main()
