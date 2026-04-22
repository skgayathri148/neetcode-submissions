class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            height = min(heights[l], heights[r])
            area = (r - l) * height
            if area > max_area:
                max_area = area
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

            