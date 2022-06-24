class Solution:
    def isHaveDuplicate(self, data: List[int]) -> bool:
        return len(list(set(data))) != len(data)
    
    def convertToListInt(self, data: List[str]) -> List[int]:
        return [int(strValue) for strValue in data if strValue != "."]
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for index in range(0, 9):
            # Row
            if self.isHaveDuplicate(self.convertToListInt(board[index])):
                return False
            # Column
            data = [board[i][index] for i in range(0, 9)]
            if self.isHaveDuplicate(self.convertToListInt(data)):
                return False
            
        # Square
        for index in range(0, 3):
            dataTb1 = self.convertToListInt(board[index*3][0:3] + board[index*3+1][0:3] + board[index*3+2][0:3])
            dataTb2 = self.convertToListInt(board[index*3][3:6] + board[index*3+1][3:6] + board[index*3+2][3:6])
            dataTb3 = self.convertToListInt(board[index*3][6:] + board[index*3+1][6:] + board[index*3+2][6:])
            
            if self.isHaveDuplicate(dataTb1) or self.isHaveDuplicate(dataTb2) or self.isHaveDuplicate(dataTb3):
                return False
            
        return True
            