class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word2_set = set(word2)
        """ 
        Words of different lengths can't be transformed into each other.
        If specific letter isn't presented in word1, .difference() length will be higher than 0.
        """
        if len(word2) != len(word1) or len(word2_set.difference(set(word1))) > 0:
            return False

        """ Initialise the storage of counted letters, their lengths will be the same as the length of word2_set """
        counted_1 = [0] * len(word2_set)
        counted_2 = counted_1.copy()

        i = 0
        for letter in word2_set:
            counted_1[i] = word1.count(letter)
            counted_2[i] = word2.count(letter)
            i += 1

        if counted_1 == counted_2: # Lists are identical, we don't need any permutations and can return True
            return True
        else:
            j = 0
            """ 
            To check whether lists are identical we need to assure that each value of one list is presented in another.
            If values are in both lists, we pop them out from lists and continue the loop, until lists are empty, 
            otherwise we return False, because second list doesn't contain required element.
            """
            while len(counted_1) > 0:
                if counted_1[j] in counted_2:
                    k = counted_2.index(counted_1[j])
                    counted_1.pop(j)
                    counted_2.pop(k)
                else:
                    return False
        """ Because loop finished, lists contained identical values, therefore they can be permuted to one another """
        return True

if __name__ == "__main__":
    s = Solution()
    assert s.closeStrings(word1 = "a", word2 = "aa") == False
    assert s.closeStrings(word1="cabbba", word2 = "abbccc") == True
    assert s.closeStrings(word1 = "abc", word2 = "bca") == True


"""
Two strings are considered close if you can attain one from the other using the following operations:
Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with 
the other character. For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.
Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 
Constraints:
1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
"""