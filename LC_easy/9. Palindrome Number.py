class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        integer solution
        """
        if x < 0:
            return False

        reversed_number = 0
        worked = x

        while worked != 0:
            last_digit = worked % 10
            reversed_number = reversed_number * 10 + last_digit
            worked //= 10

        return reversed_number == x


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(121) == True
    assert s.isPalindrome(-121) == False
    assert s.isPalindrome(10) == False


"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""