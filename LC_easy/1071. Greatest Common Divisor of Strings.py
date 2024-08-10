
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        Because we can use same function n-times required to solve the problem we can implement recursion to
        restart the function if it can be processed further.

        For this task we have x major rules:
        1. Prefix of/first string has to be equal to Prefix of/second string
        2. If we on the end of longest string, and they are equal, we return the current prefix, so to say the
        string that lasted to the end.
        3. We return empty string if we didn't find any common prefix
        """

        """
        Because in gcd task 'AbcAbc' and 'AbcAbcAbcAbc' we have to get only 'Abc' and not 'AbcAbc'
        we can check whether their sum is equal when added. Here we get recursion in handy, because we can
        change looked string until their length isn't equal.   
        """

        if str1 + str2 != str2 + str1:
            return ""

        if len(str1) == len(str2):
            return str1

        if len(str1) > len(str2):# because str1 is longer, we pass str1, but sliced from starting from str2 ending
            return self.gcdOfStrings(str1[len(str2):], str2)
        #else case
        return self.gcdOfStrings(str1, str2[len(str1):])


if __name__ == "__main__":
    s = Solution()
    assert s.gcdOfStrings(str1 = "ABCABC", str2 = "ABC") == "ABC"
    assert s.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB") == "AB"
    assert s.gcdOfStrings(str1 = "LEET", str2 = "CODE") == ""

"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""