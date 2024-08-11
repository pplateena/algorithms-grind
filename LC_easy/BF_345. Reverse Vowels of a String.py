class Solution:
    def reverseVowels(self, s: str) -> str:
        l = len(s)
        if l == 1:
            return s

        l = len(s)
        low = 0
        high = l - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        left_part, right_part = str(), str()

        while low <= high:
            while low <= high and s[low].lower() not in vowels: left_part = left_part + s[low]; low += 1

            while low <= high and s[high].lower() not in vowels: right_part = s[high] + right_part; high -= 1

            if  low <= high and s[low].lower() in vowels and s[high].lower() in vowels:
                left_part = left_part + s[high]
                right_part = s[low] + right_part

                low += 1
                high -= 1
        return left_part + right_part[-(l - len(left_part)):] if len(left_part) < l else left_part

if __name__ == "__main__":
    s = Solution()
    assert s.reverseVowels("hello") == "holle"
    assert s.reverseVowels("leetcode") == "leotcede"



"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
 

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""