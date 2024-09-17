"""
statement: Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

Input: timePoints = ["23:59","00:00"]
Output: 1

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

Constraints:
2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
"""

"""
Intuition: We have to just count time difference with closest times. To find closest times,
we just sort it and calculate minimum time difference between two neighboring time including 
first and last one as they time times in a circular way.
To calculate time, we convert the time to minutes for easier calculations. It can be counted in two ways.
One from minimum time to maximum time difference and another is to maximum to 24:00 hour then to minimum.
We calculate both and take only the minimum one.
"""

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def calculate(t,tt):
            t=t.split(":")
            tt=tt.split(":")
            
            return min(-(int(t[0])*60+int(t[1]))+int(tt[0])*60+int(tt[1])
            ,1440-(int(tt[0])*60+int(tt[1]))+int(t[0])*60+int(t[1]))

        timePoints.sort()
        res=calculate(timePoints[0],timePoints[-1])

        for i in range(1,len(timePoints)):
            res=min(res,calculate(timePoints[i-1],timePoints[i]))
        return res