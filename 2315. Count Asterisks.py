class Solution:
    def countAsterisks(self, s: str) -> int:
        if len(s) == 0:
            return 0
        data = ""
        isHave = False
        start, end = 0, 0
        while end != len(s):
            if s[end] == "|":
                if isHave == True:
                    start = end + 1
                    isHave = False
                else:
                    isHave = True
                    data += s[start: end]
            end += 1
        data += s[start: end]
        return data.count("*")