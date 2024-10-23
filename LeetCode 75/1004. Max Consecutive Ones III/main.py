from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        maxNumberOfOnes = 0
        numberOfZeroes = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                numberOfZeroes += 1

            while numberOfZeroes > k:
                if nums[i] == 0:
                    numberOfZeroes -= 1
                i += 1

            maxNumberOfOnes = max(maxNumberOfOnes, j - i + 1)

        return maxNumberOfOnes


# Test the solution
print(Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
