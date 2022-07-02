class Solution:
    def minDeletions(self, s: str) -> int:
        listChar = list(set(s))
        frequency = sorted([s.count(value) for value in listChar])
        count = 0
        for index in range(len(frequency)):
            while frequency[index] != 0 and (frequency[index] in frequency[0: index]):
                frequency[index] -= 1
                count += 1
        return count
        