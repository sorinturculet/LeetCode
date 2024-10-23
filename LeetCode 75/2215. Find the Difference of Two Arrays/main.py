from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        result = [[], []]
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result[0].append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                result[1].append(nums2[j])
                j += 1
            else:
                i += 1
                j += 1
        while i < len(nums1):
            result[0].append(nums1[i])
            i += 1
        while j < len(nums2):
            result[1].append(nums2[j])
            j += 1
        return result
print(Solution().findDifference([1, 2, 3, 4, 5], [1, 2, 3, 4])) # [[5], []]