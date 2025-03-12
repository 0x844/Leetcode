class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        pos = 0
        for i in range(len(nums)): 
            if (pos < len(nums)):
                string = ""
                orig = nums[pos]   
                
                if pos == len(nums) - 1: # if last element
                    result.append(str(orig))
                    break

                if nums[pos] + 1 == nums[pos + 1]:
                    while (pos + 1 < len(nums) and nums[pos] + 1 == nums[pos + 1]):
                        pos += 1
                    string += str(orig) + "->" + str(nums[pos])
                    result.append(string)
                    pos += 1
                else:
                    string += str(orig)
                    result.append(string)
                    pos += 1
        return result
"""
i = 0
pos = 0
string = "0->0"
orig = 0
[0,1,2,4,5,7]
 ^

"""
