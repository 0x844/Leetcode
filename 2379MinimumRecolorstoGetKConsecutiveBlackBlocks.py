class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = k - 1
        counter = []
        
        # count freq of W in each window -> min of these is the answer
        while (right < len(blocks)):
            counter.append(blocks[left:right+1].count("W"))
            left += 1
            right += 1
        return min(counter)
