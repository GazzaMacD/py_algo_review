"""
557: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

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


def reverse_words(s: str) -> str:
    words = s.split(" ")
    results = []

    def reverse_string(s: str) -> str:
        sub = list(s)
        left = 0
        right = len(sub) - 1
        while left < right:
            sub[left], sub[right] = sub[right], sub[left]
            left += 1
            right -= 1
        return "".join(sub)

    for word in words:
        rword = reverse_string(word)
        results.append(rword)
    return " ".join(results)


if __name__ == "__main__":
    # Example 1:
    s = "Let's take LeetCode contest"
    ans = "s'teL ekat edoCteeL tsetnoc"
    res = reverse_words(s)
    assert res == ans, f"func running_sum expected {ans}, got {res}"

    # Example 2:
    s = "God Ding"
    ans = "doG gniD"
    res = reverse_words(s)
    assert res == ans, f"func running_sum expected {ans}, got {res}"

    print("Success!!")
