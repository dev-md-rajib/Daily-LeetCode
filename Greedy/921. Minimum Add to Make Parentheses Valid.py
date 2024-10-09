"""
Statement: A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

"""

"""
Intuition: At any point if closing parenthesis is more than opening, we have to add an opening 
parenthesis instantly. After traversing the string, if we see opening parenthesis remained , there were not enough closing parenthesis
we have to add it to the last.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res=op=0

        for c in s:
            if c=="(":
                op+=1
            else:
                op-=1
                if op<0:
                    res+=1
                    op=0
        
        return res+max(op,0)