class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        freqMap = defaultdict(int)
        for card in hand:
            freqMap[card] += 1
        hand.sort()

        for num in hand:
            if freqMap[num]:
                for i in range(num, num + groupSize):
                    if not freqMap[i]:
                        return False
                    freqMap[i] -= 1
        return True




