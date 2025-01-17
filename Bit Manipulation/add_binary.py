class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)

        while b:
            without_carry = a ^ b
            carry = (a & b) << 1
            a, b = without_carry, carry
        
        return bin(a)[2:]
    
    # Time Complexity : O(A+B)
    # Space Complexity : O(1)