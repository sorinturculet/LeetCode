class Solution:
    def reverseWords(self, s: str) -> str:
        reversed = s.split()[::-1]
        return ' '.join(reversed)
print(Solution().reverseWords("the sky is blue"))
