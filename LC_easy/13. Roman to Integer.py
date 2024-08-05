class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # map of roman numbers
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        """
        We utilize dictionary in order to understand which number correspond to given letter.
        If previous number is higher we add it, if lesser we subtract it.
        We need to skip last element, because we can't compare it. It will always be an additive.
        """

        number = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                number -= roman[s[i]]
            else:
                number += roman[s[i]]

        return number + roman[s[-1]] # added last element

if __name__ == "__main__":
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
