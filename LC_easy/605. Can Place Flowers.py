class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i, bed in enumerate(flowerbed):
            """ 
            Because we iterate through list from left to right we possibly could have 3 scenarios:
                    1. Flower has only neighbour to the right - [Flower, Neighbour]
                    2. Flower has neighbours from both sides - [Neighbour, Flower, Neighbour]
                    3. Flower has only neighbour to the left - [Neighbour, Flower]
                
            The problem is to understand which scenario we got, and then process logic part. Requirements for 
            corresponding scenarios to happen:
                1. We can plant in checked bed, index of bed is 0, next bed is not planted.
                2. We can plant in checked bed, previous bed is 0, next bed is 0.
                3. We can plant in checked bed, index of bed is 0, next bed.
                
            As we can see, in total we have 3 requirements in total but only first is always same, 
            other two may vary. So we need to can do 'bool and (bool or bool) and (bool or bool)' construct
            that can check all possible combinations of inputs.
                
            """
            if bed == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
            """We can modify given target value to decrease Space Complexity, if we reach 0, then answer is True"""
            if n <= 0:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    assert s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1) == True
    assert s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2) == False

"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted 
in adjacent plots. Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers 
rule and false otherwise.

 

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""