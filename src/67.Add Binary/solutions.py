class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry, res = len(a) - 1, len(b) - 1, 0, ""
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])  #加入当前的bit
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            # 如果a 和 b 当前的bit 都是1 那么carry就是2 该为result就该是0因为carry over了1
            res = str(carry % 2) + res
            carry //= 2
        return res
