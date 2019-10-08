# Solution to problem at https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        is_negative = False
        if x < 0:
            x *= -1
            is_negative = True

        while x != 0:
            pop = x % 10
            x //= 10
            rev = 10 * rev + pop
        if is_negative:
            rev *= -1
        if rev > 2 ** 31 - 1 or rev <= - 2 ** 31:
            return 0
        return rev
