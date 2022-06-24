class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        listFirstData = [matrix[i][0] for i in range(0, len(matrix))]
        
        left, right = 0, len(listFirstData) - 1
        
        while left <= right:
            middle = left + (right - left) // 2
            
            if listFirstData[middle] == target:
                return True
            
            if listFirstData[middle] > target:
                right = middle - 1
            elif listFirstData[middle] < target:
                left = middle + 1
        
        row = right
        left, right = 0, len(matrix[row]) - 1

        while left <= right:
            middle = left + (right - left) // 2
            
            if matrix[row][middle] == target:
                return True
            
            if matrix[row][middle] > target:
                right = middle - 1
            elif matrix[row][middle] < target:
                left = middle + 1
                
        return False