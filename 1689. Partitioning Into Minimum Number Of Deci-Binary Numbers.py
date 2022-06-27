class Solution:
    def minPartitions(self, n: str) -> int:
        max = int(n[0])
        # 34 = 11 * 3 + 1
        # 35 = 11 * 3 + 1 + 1
        for i in range(len(n)):
            if int(n[i]) > max:
                max = int(n[i])
        return max
        
