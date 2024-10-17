from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        lst=[]
        for candy in candies:
            if candy + extraCandies>=max_candies:
                lst.append(True)
            else:
                lst.append(False)
        return lst
    def kidsWithCandies2(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]
print(Solution().kidsWithCandies([2,3,5,1,3],3))

