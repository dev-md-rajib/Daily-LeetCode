"""
Statement: Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Input: s1 = "ab", s2 = "eidbaooo"
Output: true

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

"""
Intuition: Count and compare.
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        mem=[0]*26
        for c in s1:
            mem[ord(c)-ord('a')] += 1
        tmp=[0]*26

        for i, c in enumerate(s2):
            
            tmp[ord(c)-ord('a')] += 1

            if i>=len(s1):
                offset=i-len(s1)
                tmp[ord(s2[offset])-ord('a')] -= 1

            if tmp == mem:
                return True
            
            
        return False
