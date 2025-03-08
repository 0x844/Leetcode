class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(height) - 1
        max = 0
        for i in range(len(height)):
            if height[ptr1] <= height[ptr2]:
                if max < height[ptr1] * (len(height) - (i+1)):
                    max = height[ptr1] * (len(height) - (i+1))
                ptr1 += 1
            elif height[ptr2] <= height[ptr1]:
                if max < height[ptr2] * (len(height) - (i+1)):
                    max = height[ptr2] * (len(height) - (i+1))
                ptr2-=1
        if max == 0:
            return height[0] * height[len(height) - 1]
        return max
