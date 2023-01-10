"""
Given a string s, reverse the string according to the following rules:
    All the characters that are not English letters remain in the same position.
    All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"

Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:

    1 <= s.length <= 100
    s consists of characters with ASCII values in the range [33, 122].
    s does not contain '\"' or '\\'.
"""


def reverse_only_letters(s: str) -> str:
    ans = []
    j = len(ans) - 1
    for i, x in enumerate(s):
        if x.isalpha():
            while not s[j].isalpha():
                j -= 1
                ans.append(s[j])
                j -= 1
        else:
            ans.append(x)

    return "".join(ans)


if __name__ == "__main__":
    # Example 1:
    s = "ab-cd"
    ans = "dc-ba"
    res = reverse_only_letters(s)
    assert res == ans, f"func running_sum expected {ans}, got {res}"

    print("Success!!")
