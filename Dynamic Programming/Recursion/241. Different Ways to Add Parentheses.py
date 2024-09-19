"""
statement: Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.
The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

Input: expression = "2-1-1"
Output: [0,2]

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]

Constraints:
- 1 <= expression.length <= 20
- expression consists of digits and the operator '+', '-', and '*'.
- All the integer values in the input expression are in the range [0, 99].

"""


"""
Intuition: As the constrains are low and we have to compute in different part with same operations,
this suggests the problem is recursive and can be computed by Dynamic Programming.
The approach is when we find a operator, we separate the string in two parts and compute and merge their result.
We have chosen the operator because, we always have to operate the operation, but differs with whom we
operate, as left and right side can be calculated and parenthesis used in multiple ways, we calculate every
calculation recursively and merge their result with the current operator.
"""

class Solution:
    def diffWaysToCompute(self, exp: str) -> List[int]:

        mem={}

        def compute(start,end):
            if (start,end) in mem:
                return mem[(start,end)]
            res=[]

            if start==end:
                res.append(int(exp[start]))
                return res
            
            if end-start==1 and exp[start].isdigit():
                res.append(int(exp[start:end+1]))
                return res
            
            for i in range(start,end+1):
                if exp[i].isdigit():
                    continue
                left=compute(start,i-1)
                right=compute(i+1,end)

                for val in left:
                    for val2 in right:
                        if exp[i]=="+":
                            res.append(val+val2)
                        elif exp[i]=="-":
                            res.append(val-val2)
                        else:
                            res.append(val*val2)
                
            mem[(start,end)]=res
            return res
                

        return compute(0,len(exp)-1)
