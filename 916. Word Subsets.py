class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for c in word:
                ans[ord(c) - ord('a')] += 1
            return ans

        words2Max = [0] * 26
        for value in words2:
            temp = count(value)
            for i in range(26):
                words2Max[i] = max(words2Max[i], temp[i])

        res = []
        for value in words1:
            temp = count(value)
            for i in range(26):
                if temp[i] < words2Max[i]:
                    break
            else:
                res.append(value)
        return res

