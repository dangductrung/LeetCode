class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        badVersion = 1
        while left <= right:
            pivot = left + (right - left) // 2

            if isBadVersion(pivot):
                badVersion = pivot
                right = pivot - 1
            else:
                left = pivot + 1
        return badVersion