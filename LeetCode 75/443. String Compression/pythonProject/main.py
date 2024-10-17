from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        while zero < len(nums) and nums[zero] != 0:
            zero += 1
        if zero == len(nums): # no zero
            return
        for i in range(len(nums)):
            if nums[i] != 0:
                if zero != i:
                    if zero < len(nums) and zero < i:
                        nums[i], nums[zero] = nums[zero], nums[i]
                        while zero < len(nums) and nums[zero] != 0:
                            zero += 1
print(Solution().moveZeroes([4,2,4,0,0,3,0,5,1,0]))
