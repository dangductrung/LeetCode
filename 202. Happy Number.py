class Solution:
    
    def isHappy(self, n: int) -> bool:
        storage, total = [], 0
        
        while total != 1:
            total = sum([int(value)*int(value) for value in str(n)])
            if total in storage:
                return False
            storage.append(total)
            n = total
        return True
