class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) == 0 or len(t) == 0 or len(s) != len(t):
            return False

        dict_s = dict()
        dict_t = dict()

        for letter_s, letter_t in zip(s, t):

            if letter_s in dict_s:
                dict_s[letter_s] += 1
            else:
                dict_s[letter_s] = 1

            if letter_t in dict_t:
                dict_t[letter_t] += 1
            else:
                dict_t[letter_t] = 1

        if dict_t != dict_s:
            return False
        else:
            return True


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram(s = "anagram", t = "nagaram") == True
    assert s.isAnagram(s = "rat", t = "car") == False



"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""