from typing import List


def reverse_string(s: List[str]) -> None:
    """Takes a list of strings and reverses it in place
    Time complexity: 0(n)
    Space complexity: 0(1)
    """
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def main():
    s = ["h", "e", "l", "l", "o"]
    s1 = ["H", "a", "n", "n", "a", "h"]
    reverse_string(s)
    reverse_string(s1)
    print(s)
    print(s1)


if __name__ == "__main__":
    main()
