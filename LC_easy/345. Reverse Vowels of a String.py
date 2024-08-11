class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Time complexity: O(n), because we check each element only once.
        Space complexity: O(n), because we convert string to list, s_list = list(s)
        """

        """ 
        The task is centered around replacing vowels within a given string. The easiest approach for replacing 
        two elements simultaneously is to use Two Pointers algorithm. Therefore we need to convert string to a list, 
        because string does not support positional operations, perform replacements and return string of list values. 
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = list(s)

        """ We initialise pointers' positions to start and end of the list. """
        low = 0
        high = len(s) - 1

        while low < high: # Excluding equals, to skip central position.
            """ When both pointers' values are in vowels we replace their values. """
            if s_list[low] in vowels and s_list[high] in vowels:
                s_list[low], s_list[high] = s_list[high], s_list[low]
                low += 1
                high -= 1
            """ When any of pointers' values aren't vowels we move the pointers """
            if s_list[low] not in vowels:
                low += 1
            if s_list[high] not in vowels:
                high -= 1

        return "".join(s_list)

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