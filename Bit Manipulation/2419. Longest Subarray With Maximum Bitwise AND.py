"""
Statement: You are given an integer array nums of size n.
Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.
The bitwise AND of an array is the bitwise AND of all the numbers in it.
A subarray is a contiguous sequence of elements within an array.

Input: nums = [1,2,3,3,2,2]
Output: 2

Input: nums = [1,2,3,4]
Output: 1

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
"""

"""
Intuition: We can't never get result of a AND operation higher than the highest operand.
As question asks length of maximum possible sub array where AND of them is the highest. This
suggests to find the consecutive max length of highest element of the array. Because AND operation
between only highest numbers will provide the highest AND result.
"""

# Solution

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        highest = res = cur = 0
        for num in nums:
            if highest < num:
                highest = num
                res = highest = 0

            if highest == num:
                cur += 1
            else:
                cur = 0

            res = max(res, cur)
        return res