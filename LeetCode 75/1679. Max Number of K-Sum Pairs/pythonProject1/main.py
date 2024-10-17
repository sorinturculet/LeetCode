from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        counter=0
        i=0
        j=len(nums)-1
        while(i<j):
            if nums[i]+nums[j]==k:
                counter+=1
                i+=1
                j-=1
            elif nums[i]+nums[j]>k:
                j-=1
            else:i+=1
        return counter
    def maxOperations2(self, nums: List[int], k: int) -> int:
        map
print(Solution().maxOperations([3,1,3,4,3],6)) # 2
