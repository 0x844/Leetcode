class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(31):
            if ((n & (0x1 << i)) >> i) == 1:
                count += 1
        return count
