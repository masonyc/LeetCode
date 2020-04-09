class Solution:
    def integerBreak(self, n: int) -> int:
        # 初始化Dp
        if n < 2:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        product = [0] * (n+1)
        product[0], product[1], product[2], product[3] = 0, 1, 2, 3

        for i in range(4, n+1):
            maximum = 0
            for j in range(1, (i+2) // 2):
                prod = product[j] * product[i-j]
                if prod > maximum:
                    maximum = prod
                product[i] = maximum
        return maximum
