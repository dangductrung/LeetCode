class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            if matrix[i][0] == target or matrix[i][-1] == target:
                return True
            if matrix[i][0] < target and matrix[i][-1] > target:
                left, right = 0, n - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if matrix[i][mid] == target:
                        return True
                    if matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

        return False

