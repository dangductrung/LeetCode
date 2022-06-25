class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict = {}
        for c1, c2 in zip(s, t):
            dict[c1] = dict.get(c1, 0) + 1 
            dict[c2] = dict.get(c2, 0) - 1
        
        return not any(value != 0 for value in dict.values())