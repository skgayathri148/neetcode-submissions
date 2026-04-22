class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        freq_order = list(frequency.values())
        high_freq = sorted(freq_order, reverse=True)
        k_high = high_freq[:k]

        result = []
        for key in frequency:
            if frequency[key] in k_high:
                result.append(key)

        return result
