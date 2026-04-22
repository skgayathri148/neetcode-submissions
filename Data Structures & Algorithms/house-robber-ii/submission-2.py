class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxRob(arr):
            n = len(arr)
            if n > 2:
                arr[2] += arr[0]
                for i in range(3, n):
                    arr[i] += max(arr[i - 2], arr[i - 3])
                return max(arr[n - 1], arr[n - 2])
            return max(arr)
        
        n = len(nums)
        if n > 1:
            max1 = maxRob(nums[:-1])
            max2 = maxRob(nums[1:])

            return max(max1, max2)
        return nums[0]
        
    
