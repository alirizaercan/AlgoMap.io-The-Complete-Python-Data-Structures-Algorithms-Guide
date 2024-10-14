class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        common = []
        first_str = strs[0]
        for i in range(len(first_str)):
            for s in strs:
                if i >= len(strs) or s[i] != first_str[i]:
                    return "".join(common)
        
            common.append(first_str[i])
        
        return "".join(common)