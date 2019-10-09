# Solution to https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_to_val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0
        prev = None
        for letter in s:
            if (letter in 'VX' and prev == 'I')\
                    or (letter in 'LC' and prev == 'X')\
                    or (letter in 'MD' and prev == 'C'):
                ans -= 2 * symbol_to_val[prev]
            ans += symbol_to_val[letter]
            prev = letter
        return ans
        
