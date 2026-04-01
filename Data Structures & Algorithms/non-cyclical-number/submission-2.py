class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_sq(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num = num // 10
            return res
        
        loop = []
        while True:
            n = sum_sq(n)
            print(n)
            if n == 1:
                return True
            if n in loop:
                return False
            if n not in loop:
                loop.append(n)
            