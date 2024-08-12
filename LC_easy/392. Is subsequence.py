class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sL = len(s)
        tL = len(t)
        if sL > tL:
            return False

        i, j = 0, 0
        while i < sL:

            while j < tL:
                if s[i] == t[j]:
                    i += 1
                    j += 1
                    break
                else:
                    j += 1
            else:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isSubsequence(s = "abc", t = "ahbgdc") == True
    assert s.isSubsequence(s = "axc", t = "ahbgdc") == False


"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of 
the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of 
"abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one 
to see if t has its subsequence. In this scenario, how would you change your code?
"""