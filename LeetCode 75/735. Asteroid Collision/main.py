from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for ast in asteroids:
            while True:
                if len(stack) == 0:
                    stack.append(ast)
                    break
                if stack[-1]>0 and ast>0:
                    stack.append(ast)
                    break
                elif stack[-1]<0 and ast<0:
                    stack.append(ast)
                    break
                elif stack[-1]>0 and ast<0:
                    if stack[-1]==-ast:
                        stack.pop()
                        break
                    elif stack[-1]>-ast:
                        break
                    else:
                        stack.pop()
                else: # stack[len(stack)]<0 and ast>0
                    stack.append(ast)
                    break
        return stack
print(Solution().asteroidCollision([8,-8])) # [5, 10]



