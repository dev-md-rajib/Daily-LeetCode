"""
Statement: A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

Input: nums = [6,0,8,2,1,5]
Output: 4
"""

"""
Intuition: Basic monotonic stack problem. If we encounter number n while traversing through the nums,
if stack already has smaller value in itself than number n, then upcoming any number, index of n will not be 
considered as it can't provide the maximum width. Now if n is smaller than the front of the stack, it can 
be considered for future but currently it won't provide any width as the stack only consist in a 
decreasing manner. So if the front or top one itself is bigger than n, it is not possible to have a previous number
that is smaller than the top one, and also the n.
"""

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res=0
        st=[]
        for i, n in enumerate(nums):
            if not len(st):
                st.append(i)
            elif nums[st[-1]]>n:
                st.append(i)
            else:
                for ind in range(len(st)-1,-1,-1):
                    index=st[ind]
                    if nums[index]<=n:
                        res=max(res,i-index)
                    else:
                        break
            
        
        return res