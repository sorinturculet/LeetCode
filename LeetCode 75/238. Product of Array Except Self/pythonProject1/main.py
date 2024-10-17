from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            product=1
            nOfZero=0
            for num in nums:
                if num!=0:
                    product=product*num
                else :
                    nOfZero+=1
                    if (nOfZero > 1):
                        break

            if nOfZero>1:
                return [0]*len(nums)
            else: return [product if num==0 else 0 for num in nums]
        else:
            product=1
            for num in nums:
                product=product*num
            return [product//num for num in nums]

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        productbefore=[1]*len(nums)
        productafter=[1]*len(nums)
        for i in range(1,len(nums)):
            productbefore[i]=productbefore[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            productafter[i]=productafter[i+1]*nums[i+1]
        return [productbefore[i]*productafter[i] for i in range(len(nums))]

print(Solution().productExceptSelf2([1,2,3,4]))