class Solution:
    def longestPalindrome(self, s: str) -> int:
        uniqueList = list(set(s))
        length = 0
        isHaveOdd = False

        for value in uniqueList:
            count = s.count(value)
            if (count % 2) == 0:
                length += count
            elif count > 1:
                length += count - 1
                isHaveOdd = True
            elif isHaveOdd == False:
                isHaveOdd = True
            
        if isHaveOdd: 
            return length + 1
        else:
            return length
        
        