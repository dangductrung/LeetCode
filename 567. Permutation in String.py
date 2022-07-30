class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        hash1 = [0] * 26
        hash2 = [0] * 26
        
        for char in s1:
            hash1[ord(char) - ord('a')] += 1
        
        for index in range(len(s2)):
            
            position = ord(s2[index]) - ord('a') 
            if index < len(s1):
                hash2[position] += 1
            else:
                hash2[position] += 1
                hash2[ord(s2[index - len(s1)]) - ord('a')] -= 1
            if hash1 == hash2:
                return True
        
        return False
                
            