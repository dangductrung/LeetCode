class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char, '', 1)
            else:
                return False
        return True