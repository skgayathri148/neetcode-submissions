class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        prev = [0, 0, 0]
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            prev[0] = max(prev[0], triplet[0])
            prev[1] = max(prev[1], triplet[1])
            prev[2] = max(prev[2], triplet[2])

        return prev == target