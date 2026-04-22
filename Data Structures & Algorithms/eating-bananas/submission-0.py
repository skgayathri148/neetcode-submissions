class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        optimal = max_pile
        l, r = 1, max_pile
        while l <= r:
            k = (l + r) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / k)
            if total_time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
        
