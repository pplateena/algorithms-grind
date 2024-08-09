class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = len(s)
        left_index = 0
        right_index = l - 1
        while right_index - left_index >= 1:
            left = s[left_index].lower()

            if not left.isalnum():
                left_index += 1
                continue
            right = s[right_index].lower()
            if not right.isalnum():
                right_index -= 1
                continue

            if left != right:
                return False
            else:
                left_index += 1
                right_index -= 1

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