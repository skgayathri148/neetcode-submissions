class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxProd = nums[0]
        currMax = nums[0]
        currMin = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            tmp = num * currMax
            currMax = max(num, num*currMax, num*currMin)
            currMin = min(num, tmp, num*currMin)
            maxProd = max(currMax, maxProd)
        
        return maxProd
        
