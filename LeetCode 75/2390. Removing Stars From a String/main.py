class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c != '*':
                stack.append(c)
            else:
                stack.pop()
        stack=''.join(stack)
        return stack
print(Solution().removeStars("f*a*b*c*d*e*aa")) # ['f', 'e', '*']