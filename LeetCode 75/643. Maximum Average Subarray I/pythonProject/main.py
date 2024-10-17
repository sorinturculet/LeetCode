from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if(len(nums)==1):
            return nums[0]
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k,len(nums)):
            current_sum = current_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum,current_sum)
            i+=1
        return max_sum/k
print(Solution().findMaxAverage([7,4,5,8,8,3,9,8,7,6],7))
