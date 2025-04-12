class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        for i in range(len(s)):
            found = False
            for j in range(c, len(t)):
                if (s[i] == t[j]):
                    c = j + 1
                    found = True
                    break
            if not found:
                return False
        return True

    # Time Complexity : O(T)
    # Space Complexity : O(1)