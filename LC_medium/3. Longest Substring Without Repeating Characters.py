class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        seen = {}
        left = max_found = 0

        for right in range(len(s)):
            ch = s[right]
            if ch in seen and seen[ch] >= left:  # duplicate on left window band or to the right of it
                left = seen[ch] + 1  # index of left duplicate + 1 to exclude left duplicate

            seen[ch] = right  # set index of ch /reset index of found duplicate
            max_found = max(max_found, right - left + 1)  # window we are looking + 1 to compensate the idx vs len diff
        return max_found

if __name__ == "__main__":

    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3


"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.
"""