from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int: # brute force
        count=0
        for i in range(len(grid)):
            row=','.join(map(str, grid[i]))
            for j in range(len(grid)):
                col = ','.join(str(grid[k][j]) for k in range(len(grid)))
                if row == col:
                    count += 1
        return count
    def equalPairs(self, grid: List[List[int]]) -> int: # use a dictionary and compare the string of the row and column
        n=len(grid)
        count=0
        dic={}
        for i in range(n):
            dic[str(grid[i])]=dic.get(str(grid[i]),0)+1
        for i in range(n):
            tmp_lst=[]
            for j in range(n):
                tmp_lst.append(grid[j][i])
            count+=dic.get(str(tmp_lst),0)
        return count
print(Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]])) # 1