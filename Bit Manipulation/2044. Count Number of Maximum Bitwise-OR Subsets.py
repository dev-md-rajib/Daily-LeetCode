"""
Statement: Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
"""

"""
Intuition: MAx will be or of all number. find the nums.
"""

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_val = 0

        for n in nums:
            max_val |= n
        
        def countSub(pos, cur):
            if pos == len(nums):
                return 1 if cur == max_val else 0

            
            include_count = countSub(pos + 1, cur | nums[pos])
            skip_count = countSub(pos + 1, cur)  
            
            return include_count + skip_count
        
        return countSub(0, 0)
