class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if len(strs) == 1:
            return strs[0] if len(strs[0]) > 0 else ""
        rao = tuple(strs)
        if len(rao) > 2:
            first, last, *middle = rao
        else:
            first, last = rao

        min_len = min(len(first), len(last))

        prefix = None

        for i in range(min_len):

            if first == last:
                prefix = first
                break
            elif first[i] == last[i]:

                prefix = first[i] if prefix is None else prefix + first[i]

            else:
                break

        if prefix is None:
            return ""
        Done = False

        while not Done and len(rao) > 2:
            for string in middle:
                if string[:len(prefix)] != prefix:
                    prefix = prefix[:-1]

                    if len(prefix) == 0:
                        return ""

                    if first[:len(prefix)] != last[:len(prefix)]:

                        prefix = prefix[:-1]

                        if len(prefix) == 0:
                            return ""

                    Done = False
                    break

                else:
                    Done = True

        return prefix

if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert s.longestCommonPrefix(["dog","racecar","car"]) == ""


"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""