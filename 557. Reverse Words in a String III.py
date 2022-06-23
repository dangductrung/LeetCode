class Solution:
    def reverseString(self, s: List[str]) -> str:
        left, right = 0, len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -=1 
        return "".join(s)
            
    def reverseWords(self, s: str) -> str:
        result = ""
        data = [self.reverseString(list(value)) for value in s.split(" ")]
        return " ".join(data)