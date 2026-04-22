class Solution:
    def climbStairs(self, n: int) -> int:
        oneDown, twoDown = 1, 1
        
        for i in range(n - 1):
            temp = oneDown
            oneDown = oneDown + twoDown
            twoDown = temp

        return oneDown
