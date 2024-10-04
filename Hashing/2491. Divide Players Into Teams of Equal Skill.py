"""
Statement: You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

Input: skill = [3,2,5,1,3,4]
Output: 22

Input: skill = [1,1,2,3]
Output: -1
"""

"""
Intuition: We have to find the avg or target. Then check if all can be made to the target. Can be done by
hashing or sorting. For sorting the smallest and the largest will be in the same group. Have to check their sum.
"""

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        avg=sum(skill)/(len(skill)/2)
        if int(avg)!=avg:
            return -1
        counter=Counter(skill)
        res=0

        for num in skill:
            if counter[num]:
                req=avg-num
                if not counter[req]:
                    return -1
                counter[num]-=1
                counter[req]-=1
                res += (req*num)
        
        return int(res)