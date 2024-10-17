from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if(len(nums)<3):
            return False
        s1=pow(2,31)-1
        s2=pow(2,31)-1
        for num in nums:
            if(num<=s1):
                s1=num
            elif(num<=s2):
                s2=num
            else: return True
        return False
print(Solution().increasingTriplet([1,2,3,4,5])) #Output: True