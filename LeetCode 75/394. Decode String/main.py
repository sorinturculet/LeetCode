from typing import List
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        out=""
        for char in s:
            stack.append(char)
            if stack[-1]==']':
                nOfBrackes=1
                while nOfBrackes>0:
                    stackChar=stack.pop()
                    if stackChar!= '[':
                        out.