class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * 10 ** (len(digits) - 1 - i)
        num += 1
        res = []
        while num > 0:
            res = [num % 10] + res
            num = num // 10
        return res