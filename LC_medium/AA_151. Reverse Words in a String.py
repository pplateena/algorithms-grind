class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Brute approach, without converting string to list, however utilizing Two Pointer algorithm in a keen way.
        Comes closer to 'Follow up problem' that suggests making a Space Complexity O(1), as far as I understand,
        this solution has O(m) Space Complexity, where m is longest string.

        Generally a bit slower, quite inadequate, but reliable solution.
        """
        final = str()
        l = len(s) - 1
        i = 0


        while i <= l:

            if s[i] != " ":
                j = i + 1
                appendable = s[i]

                while j <= l:
                    print(j, 'j')
                    if s[j] != " " and j != l:

                        appendable = appendable + s[j]
                        j += 1
                    elif j == l:
                        final = appendable + s[j] + final if s[j] != " " else appendable + final
                        return final


                    elif s[j] == " " and j != l:
                        j += 1
                        while j <= l:
                            if s[j] != " ":
                                break
                            else:
                                j+=1

                        if j > l:
                            final = appendable + final
                            return final
                        elif j == l:
                            final = s[j] + ' ' + appendable + final
                            return final
                        else:
                            final = " " + appendable + final
                            i = j
                            break

            else:
                i += 1

        return final

if __name__ == "__main__":
    s = Solution()
    assert s.reverseWords(s = " asdasd df f") == "f df asdasd"

"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
"""