class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if len(strs) == 1:
            return [strs]

        duplicates_dict = {}  # defaultdict of list
        for n in strs:  # maybe sort a string
            chars_list = list(n)
            chars_sorted = sorted(chars_list)
            chars_tuple = tuple(chars_sorted)

            if chars_tuple in duplicates_dict:  # .keys()
                duplicates_dict[chars_tuple] += [n]
            else:
                duplicates_dict[chars_tuple] = [n]

        answer = []

        for value in duplicates_dict.values():
            answer.append(value)
        print(answer)
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""