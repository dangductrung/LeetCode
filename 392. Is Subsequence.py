class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True
        
        listChar = s
        temp = t
        while len(temp) > 0:
            if len(listChar) == 0:
                return True
            position = temp.find(listChar[0])
            
            if position < 0:
                return False
            
            listChar = listChar[1:]
            temp = temp[position + 1:]
            
        return len(listChar) == 0
            
        
            