class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26
        for c in word1:
            freq1[ord(c) - ord('a')] += 1
        for c in word2:
            freq2[ord(c) - ord('a')] += 1
        for i in range(26):
            if freq1[i]==0 and freq2[i]!=0 or freq1[i]!=0 and freq2[i]==0:
               return False
        if set(freq1) != set(freq2):
            return False
        if sorted(freq1)!=sorted(freq2):
            return False
        return True

print(Solution().closeStrings("abca","bcac")) # True