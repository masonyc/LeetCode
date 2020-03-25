class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # 设置初始值
        sum, prod = 0, 1
        while n:
            # n // 10 n % 10
            n, digit = divmod(n, 10)
            sum += digit
            prod *= digit
        return prod - sum
