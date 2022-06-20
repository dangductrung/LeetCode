class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = ""
        
        firstValue = strs[0]
        lastValue = strs[-1]
       
        length = min(len(firstValue), len(lastValue))
        
        for i in range(0, length):
            if firstValue[i] == lastValue[i]:
                result += firstValue[i]
            else:
                return result
        return result
        