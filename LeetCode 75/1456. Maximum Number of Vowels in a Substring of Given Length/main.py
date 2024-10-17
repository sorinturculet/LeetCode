class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        nOfVowels=0
        for i in range(k-1):
           if s[i] in vowels:
               nOfVowels+=1
        maxvowels=nOfVowels
        for i in range(k-1,len(s)):
            if s[i] in vowels:
                nOfVowels += 1
            if(nOfVowels>=k):
                return k
            maxvowels=max(maxvowels,nOfVowels)
            if s[i-k+1] in vowels:
                nOfVowels -= 1
        return maxvowels
print(Solution().maxVowels("weallloveyou",7)) # 3