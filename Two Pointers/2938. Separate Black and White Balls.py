"""
Statement: There are n balls on a table, each ball has a color black or white.

You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.

In each step, you can choose two adjacent balls and swap them.

Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.

Input: s = "101"
Output: 1

Constraints:

1 <= n == s.length <= 105
s[i] is either '0' or '1'.
"""

"""
Intuition: No zero can't be on the right. If we find a zero, all the black balls at right has to be
swapped to the right. So count how many black encountered and count swap if encounter zero.
"""

class Solution:
    def minimumSteps(self, s: str) -> int:
        res, black = 0, 0
        
        for c in s:
            if c=='0':
                res += black
            else:
                black += 1
        
        return res