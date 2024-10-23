from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        nOfZeroes=0
        maxlength=0
        for j in range(len(nums)):
            if nums[j]==0:
                nOfZeroes+=1
            while nOfZeroes > 1:
                if nums[i]==0:
                    nOfZeroes-=1
                i+=1
            maxlength=max(maxlength,j-i+1)
        return maxlength-1
print(Solution().longestSubarray([1,1,0,0,1,1,1,0,1])) # 5