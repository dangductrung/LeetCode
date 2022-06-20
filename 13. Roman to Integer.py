class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        result = 0
        remain = 0
        beforeValue = hashMap[s[0]]
        for item in s:
            value = hashMap[item]
            if value < beforeValue:
                result += remain
                remain = value
            elif value == beforeValue:
                remain += value
            else:
                result += value - remain
                remain = 0
            beforeValue = value
        if remain > 0:
            result += remain
        return result
        