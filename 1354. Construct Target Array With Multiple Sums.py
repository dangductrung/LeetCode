class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1 and target[0] != 1:
            return False
        target.sort(reverse = True)
        while target[0] != 1:
            total = sum(target)
            value = target[0]
            if (total - value) == 1:
                return True
            remain = value % (total - value)
            if remain == 0 or remain == value:
                return False
            target.pop(0)
            target.append(remain)
            target.sort(reverse = True)

        return True