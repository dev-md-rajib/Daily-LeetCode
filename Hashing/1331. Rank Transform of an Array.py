"""
Statement: Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.

Input: arr = [40,10,20,30]
Output: [4,1,2,3]

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
"""

"""
Intuition: Basic counting, sorting problem. Remove the duplicates, sort to find the rank and use them for the arr.

"""

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        nums = sorted(set(arr))
        rank = 1
        for num in nums:
            ranks[num] = rank
            rank += 1
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]
        return arr