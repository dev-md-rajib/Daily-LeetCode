"""
Statement:You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

"""

"""
Intuition: Keep a window of size k. When redundant , when redundant found remove it.
"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        res=0
        cur=0
        left=0
        right=0
        mem=defaultdict(int)
        
        while right<len(nums):
            cur+=nums[right]
            mem[nums[right]]+=1
            
            if mem[nums[right]]>1:
                while mem[nums[right]]>1:
                    mem[nums[left]]-=1
                    cur-=nums[left]
                    left+=1
            if right-left+1>k:
                mem[nums[left]]-=1
                cur-=nums[left]
                left+=1
            if right-left+1==k:
                res=max(cur,res)
            right+=1
            
                
            
        return res