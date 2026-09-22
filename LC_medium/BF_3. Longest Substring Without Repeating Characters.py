from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l < 2:
            return l

        # max_found

        current_letters = set()
        max_found = 0

        for idx, n in enumerate(s):
            if n in current_letters:
                max_found = max(len(current_letters), max_found)

                left = s.find(n, idx - len(current_letters), idx) + 1
                right = idx
                sliced_s = s[left:right + 1]
                current_letters = set(sliced_s)
                # first dup in left, slice string from it to current = set
            else:
                current_letters.add(n)

        return max(len(current_letters), max_found)

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