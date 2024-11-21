"""
Statement: You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.


"""


"""
Intuition: Remove the largest one possible.

"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        a=s.count('a')
        b=s.count('b')
        c=len(s)-(a+b)
        
        if min(a,b,c)<k:return -1
        
        a-=k
        b-=k
        c-=k
        able =[a,b,c]
        cur=[0]*3
        left=right=res=0
        
        while right<len(s):
            ind=ord(s[right])-ord('a')
            cur[ind]+=1
            while cur[ind]>able[ind]:
                IND=ord(s[left])-ord('a')
                cur[IND]-=1
                left+=1
            res=max(res,sum(cur))
            right+=1
            
        return len(s)-res
        
        