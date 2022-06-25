class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Array contain repeat time of char
        data = {}
        for char in s:
            if char not in data.keys():
                data[char] = 0
            data[char] += 1
            
        try:
            index = list(data.values()).index(1)
            return s.index(list(data.keys())[index])
        except:
            return -1