class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        out = []
        while len(asteroids) > 0:
            if len(out) == 0:
                out.append(asteroids.pop(0))

            if len(asteroids) > 0 and out[-1] * asteroids[0] < 0 and out[-1] > 0:

                if abs(out[-1]) < abs(asteroids[0]):
                    out.pop()

                elif abs(out[-1]) > abs(asteroids[0]):
                    asteroids.pop(0)
                else:
                    out.pop()
                    asteroids.pop(0)
            elif len(asteroids) == 0:
                return out
            else:
                out.append(asteroids.pop(0))

        return out


if __name__ == "__main__":
    s = Solution()
    assert s.asteroidCollision([5,10,-5]) == [5,10]
    assert s.asteroidCollision([10,2,-5]) == [10]


"""
We are given an array asteroids of integers representing asteroids in a row. For each asteroid, the absolute 
value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions. 
If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

 

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:
2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""