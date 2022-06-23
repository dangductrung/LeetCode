class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1 or len(s) == 0:
            return len(s)
        listStr, pivot, temp = [], 0 , ""
        while pivot != len(s):
            if s[pivot] not in temp:
                temp += s[pivot]
            else:
                listStr.append(temp)
                
                keyword = s[pivot]
                last = listStr[len(listStr) - 1]
                temp = last[last.index(keyword) + 1: ] + keyword
            
            pivot += 1
            
        listStr.append(temp)
        return max([len(value) for value in listStr])