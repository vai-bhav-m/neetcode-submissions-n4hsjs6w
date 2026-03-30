class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s)-1
        while p1 < len(s) and p2 >= 0:
            if s[p1].isalnum() == False:
                p1 += 1
                continue
            if s[p2].isalnum() == False:
                p2 -= 1
                continue
            if p2 <= p1:
                return True
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        return True
