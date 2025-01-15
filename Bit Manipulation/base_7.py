class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'

        originial_num = num
        num = abs(num)
        remainders = []

        while num > 0:
            remainder = num % 7
            remainders.append(str(remainder))
            num //= 7

        if originial_num < 0:
            remainders.append('-')
        remainders.reverse()
        return ''.join(remainders)

    # Time Complexity : O(log_7(N))
    # Space Complexity : O(log_7(N))