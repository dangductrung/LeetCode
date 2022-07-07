class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @cache
        def check(str1: str, str2: str, str3: str):
            l1, l2, l3 = len(str1), len(str2), len(str3)
            if l3 != (l1 + l2) :
                return False
            if l1 == l2 == l3 == 0:
                return True
            if l1 == 0:
                return str2 == str3
            if l2 == 0:
                return str1 == str3
            
            if str1[0] == str2[0] == str3[0]:
                return check(str1[1:], str2, str3[1:]) or check(str1, str2[1:], str3[1:])
            if str1[0] == str3[0]:
                return check(str1[1:], str2, str3[1:])
            if str2[0] == str3[0]:
                return check(str1, str2[1:], str3[1:])
            return False
        return check(s1, s2, s3)
