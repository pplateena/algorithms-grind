class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        substring = list(s[:k])
        max_counted = 0

        for letter in vowels:
            if letter in substring:
                max_counted += substring.count(letter)
        current_counted = max_counted

        for i in range(k, len(s)):

            if substring.pop(0) in vowels:
                current_counted -= 1

            substring += [s[i]]
            if s[i] in vowels:
                current_counted += 1

            max_counted = max(max_counted, current_counted)
            if max_counted == current_counted:
                current_counted = max_counted

        return max_counted


if __name__ == "__main__":
    s = Solution()
    assert s.maxVowels(s = "abciiidef", k = 3) == 3
    assert s.maxVowels(s = "aeiou", k = 2) == 2
    assert s.maxVowels(s = "leetcode", k = 3) == 2



"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 
Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""