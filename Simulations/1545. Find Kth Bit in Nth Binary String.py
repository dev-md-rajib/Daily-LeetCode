""""
Statement: Given two positive integers n and k, the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.
"""

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"

        def generate(s):
            sub=""
            
            for i in range(len(s)-1,-1,-1):
                if s[i]=='1':
                    sub += '0'
                else:
                    sub += '1'
            
            return sub

        for i in range(1,n):

            s += "1" + generate(s)

        print(s)
        return s[k-1]