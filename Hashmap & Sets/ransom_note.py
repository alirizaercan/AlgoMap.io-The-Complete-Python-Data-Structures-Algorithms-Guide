class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine)
        
        for ch in ransomNote:
            if hashmap[ch] > 0:
                hashmap[ch] -= 1
            else:
                return False
        return True
    

        # Time Complexity : O(m+n)
        # Space Complexity : O(n)