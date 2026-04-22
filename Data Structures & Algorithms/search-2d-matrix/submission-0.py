class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            search = (top + bottom) // 2
            if matrix[search][0] <= target and matrix[search][-1] >= target:
                break
            elif matrix[search][0] > target:
                bottom = search - 1
            else:
                top = search + 1

        if not top <= bottom:
            return False

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[search][mid] == target:
                return True
            elif matrix[search][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False