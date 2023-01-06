from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    curr = 0
    for i in range(k):
        curr += nums[i]
    ans = curr / k
    for j in range(k, len(nums)):
        curr += nums[j] - nums[j - k]
        print(curr)
        ans = max(ans, (curr / k))
    return ans


if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    nums1 = [5]
    k1 = 1
    print(find_max_average(nums, k))
    print(find_max_average(nums1, k1))
