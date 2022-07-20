class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubsequen(src: str, word:  str):
            if len(src) < len(word):
                return False
            if src == word:
                return True
            listChar = word
            temp = src
            while len(temp) > 0:
                if len(listChar) == 0:
                    return True
                position = temp.find(listChar[0])

                if position < 0:
                    return False
                listChar = listChar[1:]
                temp = temp[position + 1:]
            return len(listChar) == 0
        result = 0
        for word in words:
            if isSubsequen(s, word):
                result += 1
        return result
