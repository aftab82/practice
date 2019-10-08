# Solution to https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        while x > rev:
            rev = 10 * rev + x % 10
            x //= 10

        return rev == x or x == rev // 10
