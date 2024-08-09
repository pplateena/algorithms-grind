class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # limited to 2 types
        # left to right
        # free to start from any position

        l = len(fruits)
        if l < 3:
            return l
        i = 0
        max_len = 0
        while i <= l - 2:
            if max_len > l - i:
                break
            max_found = 1
            j = i + 1
            first_type = fruits[i]
            second_type = fruits[j]

            while first_type == second_type and j < l - 1: j += 1; max_found += 1; second_type = fruits[j]

            while (j != l) and (fruits[j] == first_type or fruits[j] == second_type): j += 1; max_found += 1;
            max_len = max(max_found, max_len)

            i += 1

        return max_len


if __name__ == "__main__":
    s = Solution()
    assert s.totalFruit([1,2,1]) == 3
    assert s.totalFruit([0,1,2,2]) == 3
    assert s.totalFruit([1,2,3,2,2]) == 4


"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by 
an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit 
each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while 
moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:
1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
"""