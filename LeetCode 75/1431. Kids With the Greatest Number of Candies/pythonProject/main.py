from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(n==0):
            return True
        if(len(flowerbed)==1):
            if(flowerbed[0]==0):
                return True
            else:
                return False
        counter=0
        for i in range(len(flowerbed)):
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    counter+=1
            elif i==len(flowerbed)-1:
                if flowerbed[i-1]==0 and flowerbed[i]==0:
                    flowerbed[i]=1
                    counter+=1
            else:
                if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    counter+=1
        return counter>=n
print(Solution().canPlaceFlowers([1,0,0,0,1],1)) # 2
