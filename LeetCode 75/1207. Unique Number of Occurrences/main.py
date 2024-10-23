from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in arr:
            count[i] = count.get(i, 0) + 1
        for key,value in count.items():
            for key2,value2 in count.items():
                if key != key2 and value == value2:
                    return False
        return True
print(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3])) # True