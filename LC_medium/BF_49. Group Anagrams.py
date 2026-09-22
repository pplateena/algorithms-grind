class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        if len(strs) == 1:
            return [strs]

        anagrams_set = set()
        output_dict = dict()

        for i, word in enumerate(strs):

            letters = tuple(sorted(letter for letter in word))

            if letters not in anagrams_set:
                anagrams_set.add(letters)
                output_dict[letters] = [word]
            else:
                output_dict[letters] += [word]

        return [word_list for word_list in output_dict.values()]


if __name__ == "__main__":
    s = Solution()
    ## requires to implent sorted() for correct assertion, in order to accept different combination of same lists
    # assert s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]
    # assert s.groupAnagrams([""]) == [[""]]
    # assert s.groupAnagrams(["a"]) == [["a"]]

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
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