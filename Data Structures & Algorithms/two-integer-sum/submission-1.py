class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToInd = {}
        for i, num in enumerate(nums):
            if target - num in numToInd:
                return [numToInd[target - num], i]
            numToInd[num] = i
            
