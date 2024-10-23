from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_alt = 0
        max_alt = 0
        for alt in gain:
            current_alt+=alt
            max_alt=max(max_alt,current_alt)
        return max_alt
print(Solution().largestAltitude([-5,1,5,0,-7])) # 1

