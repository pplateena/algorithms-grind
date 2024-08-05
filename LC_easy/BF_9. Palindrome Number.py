class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        String solution
        """

        if x < 0:
            return False

        x = str(x)

        if len(x) == 1:
            return True
        elif len(x) in range(2, 3):

            if x[0] == x[-1]:
                return True
            else:
                return False

        first, *middle, last = tuple(number for number in x)

        if first == last and len(middle) == 1:
            return True
        elif first == last:
            reversed_middle = middle.copy()
            reversed_middle.reverse()
            for i in range(len(reversed_middle)):
                if middle[i] != reversed_middle[i]:
                    return False
        else:
            return False

        return True


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