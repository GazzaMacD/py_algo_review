def is_palindrome(s: str) -> bool:
    """Returns true if string is palindrome"""
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def brute_has_target(nums, targ):
    """Brute force check, has 0(n2) complexity"""
    for n in nums:
        for j in nums:
            if n + j == targ:
                return True
    return False


def tp_has_target(nums: list[int], targ: int) -> bool:
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == targ:
            return True
        if curr > targ:
            right -= 1
        else:
            left += 1

    return False


def is_subsequence(sub: str, string: str) -> bool:
    i = 0
    j = 0
    while i < len(sub) and j < len(string):
        if sub[i] == string[j]:
            i += 1
        j += 1
    return i == len(sub)


def main() -> None:
    pal1 = "racecar"
    pal2 = "raccar"
    npal1 = "rbcecar"
    print(is_palindrome(pal1))
    print(is_palindrome(pal2))
    print(is_palindrome(npal1))
    nums = [1, 2, 4, 6, 8, 9, 14, 15]
    target = 13
    print(brute_has_target(nums, target))
    print(tp_has_target(nums, target))
    lng = "abcde"
    sub = "ace"
    print("Is Subsequence", is_subsequence(sub, lng))


if __name__ == "__main__":
    main()
