from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightsum = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            if leftsum == rightsum - nums[i]:
                return i
            leftsum += nums[i]
            rightsum -= nums[i]
        return -1
print(Solution().pivotIndex([1, 7, 3, 6, 5, 6])) # 3