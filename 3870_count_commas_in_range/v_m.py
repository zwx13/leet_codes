class Solution:
    def countCommas(self, n: int) -> int:
        str_n = str(n)
        
        if len(str_n) < 4:
            return 0

        return n - 1000 + 1