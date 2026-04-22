class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            dist = - ((point[0]**2) + (point[1]**2))
            heapq.heappush(res, [dist, point])
            if len(res) > k:
                heapq.heappop(res)
        
        result = []
        while res:
            dist, point = heapq.heappop(res)
            result.append(point)
        return result