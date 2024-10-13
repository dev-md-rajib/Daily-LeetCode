"""
Statement: You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].

You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.

Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3

Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
Output: 1
"""

"""
Intuition: Think in a reversed way. Maximum interval group at a particular point will cause,
them to create separate groups. Others group can be fit in these groups. So, the maximum number of
interval intersect will be the number of groups.
"""

class Solution:
    def minGroups(self, vals: List[List[int]]) -> int:
        start, end=[], []

        for s ,e in vals:
            start.append(s)
            end.append(e)
        
        start.sort()
        end.sort()

        i,j=0,0
        groups,res=0,0

        while i<len(start):
            if start[i]<=end[j]:
                groups+=1
                i+=1
            else:
                groups-=1
                j+=1
            res=max(res,groups)
        
        return res
