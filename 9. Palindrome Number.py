class Solution:
    def isPalindrome(self, x: int) -> bool:
        index_tail = len(str(x)) - 1
        for index_head in range(0, len(str(x))//2):
            if(str(x)[index_head] != str(x)[index_tail]):
                return False
            index_tail -= 1
        return True
        