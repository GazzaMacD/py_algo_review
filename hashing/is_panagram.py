"""
A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false
"""


def is_pangram(sentence: str) -> bool:
    return len(set(sentence)) == 26


if __name__ == "__main__":
    s = "thequickbrownfoxjumpsoverthelazydog"
    ans = True
    res = is_pangram(s)
    assert res == True, f"is_panagram gave {res}, expected {ans}"

    s = "thelazydog"
    ans = False
    res = is_pangram(s)
    assert res == False, f"is_panagram gave {res}, expected {ans}"

    print("Success!")
