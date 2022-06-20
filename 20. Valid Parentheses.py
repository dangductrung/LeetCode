class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
    
        if s[0] not in hashMap.keys() or s[len(s) - 1] in hashMap.keys():
            return False
        
        stack = []
        index = 0
        while index < len(s):
            if s[index] in hashMap.keys():
                stack.append(s[index])
            else:
                if(len(stack) == 0):
                    return False
                openValue = stack.pop()
                if hashMap[openValue] != s[index]:
                    return False
            index += 1
        return len(stack) == 0