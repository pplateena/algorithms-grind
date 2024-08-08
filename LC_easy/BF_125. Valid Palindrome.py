class Solution:
    def isPalindrome(self, s: str) -> bool:

        alphabet = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                    'z', 'x', 'c', 'v', 'b', 'n', 'm', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

        clearing_index = 0
        s = [letter.lower() for letter in s]

        while clearing_index != len(s):

            if len(s) == 0:
                break

            if s[clearing_index] in alphabet:

                clearing_index += 1
            else:
                s.pop(clearing_index)

        index = 0
        reverse_index = -1

        while index in range(len(s) // 2):

            if s[index] != s[reverse_index]:
                return False
            else:
                index += 1
                reverse_index -= 1

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") == True
    assert s.isPalindrome("1P") == False
    assert s.isPalindrome("!bHvX!?!!vHbX") == False


"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""