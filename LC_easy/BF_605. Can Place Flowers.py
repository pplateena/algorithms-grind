class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        can_plant = 0
        last_index = len(flowerbed) - 1
        if last_index == 0:
            if flowerbed[0] == 0:
                can_plant += 1
            return True if can_plant >= n else False
        elif last_index == 1:
            if sum(flowerbed) < 1:
                can_plant += 1
            return True if can_plant >= n else False

        for i, value in enumerate(flowerbed):
            if value == 0:

                if i == 0:
                    if flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        can_plant += 1
                    continue

                elif i == last_index:

                    if flowerbed[i - 1] == 0:
                        can_plant += 1

                    break

                elif i - 1 < 0 or i + 1 > last_index:
                    continue


                if flowerbed[i - 1] + flowerbed[i + 1] < 1:
                    flowerbed[i] = 1
                    can_plant += 1

            if can_plant == n:
                return True

        return True if can_plant >= n else False


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