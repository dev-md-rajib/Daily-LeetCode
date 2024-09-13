"""
Statement: 
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.

Example 1:
Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 

Example 2:
Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]
"""

"""
Intuition: We will use similar method to prefix sum. let total XOR is totalXOR. let , we have to find xor of u,v.
let xor till u is uxor and xor after v to end is vxor. And our result is res. So the totalXOR
can be divided as totalXOR = uxor xor res xor vxor. We have to find res from here. If we do
xor with totalXOR and uxor, vxor, we will find res as : uxor ^ res ^ vxor ^ uxor ^ vxor= res
"""

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        res=[]
        preXor=[]
        pre=0
        
        for i in range(len(arr)):
            pre^=arr[i]
            preXor.append(pre)
            
        for u,v in queries:
            left=0
            if u>0:
                left=preXor[u-1]
            cur=left^preXor[v]
            res.append(cur)
            
        return res
        
        