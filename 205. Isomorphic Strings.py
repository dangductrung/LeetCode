class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        
        for index in range(0, len(s)):
            if s[index] in dict:
                if (t[index] != dict[s[index]]):
                    return False
            elif t[index] in dict.values():
                positionValue = list(dict.values()).index(t[index])
                keyValue = list(dict.keys())[positionValue]
                
                if s[index] != keyValue:
                    return False
            else:
                dict[s[index]] = t[index]
                
        return True
                
            