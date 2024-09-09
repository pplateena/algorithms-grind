class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            ## Keep adding to Stack until a ']'
            if char != "]":
                stack.append(char)

            else:
                ## Extracting SubString to be Multiplied
                curr_str = ""
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str
                ## Pop to remove '['
                stack.pop()

                ## Extract full number (handles multi-digit, e.g. 10)
                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num

                ## Updating Stack with multiplied string
                curr_str = int(curr_num) * curr_str
                stack.append(curr_str)

        return "".join(stack)


if __name__ == "__main__":
    s = Solution()
    assert s.decodeString(s = "3[a]2[bc]") == "aaabcbc"
    assert s.decodeString(s = "3[a2[c]]") == "accaccacc"
    assert s.decodeString(s = "2[abc]3[cd]ef") == "abcabccdcdcdef"


"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly 
k times. Note that k is guaranteed to be a positive integer. You may assume that the input string is always valid; 
there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original
data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not 
be input like 3a or 2[4]. The test cases are generated so that the length of the output will never exceed 105.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""