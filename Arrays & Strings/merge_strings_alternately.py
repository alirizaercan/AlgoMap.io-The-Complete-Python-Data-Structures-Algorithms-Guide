class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        n1, n2 = len(word1), len(word2)
        for i in range(min(n1,n2)):
            merged += word1[i]
            merged += word2[i]
        
        merged += word1[n2:] if n1 > n2 else word2[n1:]

        return merged