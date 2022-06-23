class Solution:
    def generateSubList(self, parentList: List[int]) -> List[int]:
        return [1] + [parentList[index] + parentList[index + 1] for index in range(0, len(parentList) - 1)] + [1]
            
        
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        
        if numRows == 1:
            return result
        
        while len(result) < numRows:
            result.append(self.generateSubList(result[len(result) - 1]))
        
        return result
        