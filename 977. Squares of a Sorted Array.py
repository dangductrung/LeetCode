class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list = [value * value for value in nums]
        list.sort()
        return list