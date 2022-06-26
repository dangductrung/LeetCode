class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints[0:k])
        maxValue = total
        for i in range(k):
            left, right = k-i-1, len(cardPoints) - i - 1
            total = total - cardPoints[left] + cardPoints[right]
            maxValue = max(maxValue, total)
        return maxValue