class Solution:
    def reverseBits(self, n: int) -> int:
        constructed = 0;
        for _ in range(31):
            bit = n & 1;
            n = n >> 1;
            constructed += bit
            constructed = constructed << 1
        bit = n & 1;
        constructed += bit
        return constructed;