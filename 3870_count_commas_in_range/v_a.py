class Solution:
    def countCommas(self, n: int) -> int:
        n -= 1000
        return (0 if n < 0 else n + 1)
