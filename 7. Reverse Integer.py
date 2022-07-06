class Solution:
    def reverse(self, x: int) -> int:
        if x < 10 and x >= 0:
            return x
        data = list(str(x))
        start, end = 0, len(data) - 1
        if data[start] == "-":
            start += 1
        while data[end] == "0":
            data = data[0: end]
            end -= 1
        
        while start < end:
            temp = data[start]
            data[start] = data[end]
            data[end] = temp
            start += 1
            end -= 1
        value = int("".join(data))
        if value >= -2**31 and value <= (2**31 - 1):
            return value
        return 0
        
