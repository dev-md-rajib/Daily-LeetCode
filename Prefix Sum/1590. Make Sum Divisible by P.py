"""
Statement: Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

Input: nums = [3,1,4,2], p = 6
Output: 1

Input: nums = [6,3,5,2], p = 9
Output: 2
"""

"""
Intuition: We have to remove the extra from the total of the array. We can calculate it by using %P.
After that, loop through first to last. Last means here we will try to remove last. And we have to find from where to start.
Let, we will remove [start:last]. Now [:last] sum can be calculated while looping. Let it as pre.
sum of [start:last]%P have to be extra. Now, till current index we have to find from where we can start. To find start,
we can calculate it like from 0 to first the sum have to be (pre - extra )%p. We there can be case where extra>pre, so we will add extra P. It will not cause extra sum
as we will do %P. Then calculate size from first to last.

"""

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        extra = total % p

        if extra == 0:
            return 0

        mem = {0: -1} 
        pre = 0
        ans = float('inf')

        for i, num in enumerate(nums):
            pre += num
            pre %= p  

            target = (pre - extra + p) % p

            if target in mem:
                ans = min(ans, i - mem[target])

            mem[pre] = i

        return -1 if ans == float('inf') or ans == len(nums) else ans
