class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        listData = []
        result = []
        for value in mat:
            listData = listData + value
            
        if len(listData) != (r*c):
            return mat
        
        for i in range(0, r):
            result.append(listData[i*c: i*c + c])
        return result