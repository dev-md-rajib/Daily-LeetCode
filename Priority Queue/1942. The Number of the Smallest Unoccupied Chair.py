"""
Statement: There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.

Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1

Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
Output: 2
"""

"""
Intuition: We have to take keep track of which friends are arriving and leaking before the target
friend. We we allocate them min chair, which will be keep tracked by a queue. While arriving a new friend 
,always check which friends are leaving before him and free the chair. This way, find which chair the target friend gets.

"""

#Editorial
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_arrival = times[targetFriend][0]
        times = sorted(
            [
                (arrival, leave, index)
                for index, (arrival, leave) in enumerate(times)
            ]
        )

        next_chair = 0
        available_chairs = []
        leaving_queue = []

        for time in times:
            arrival, leave, index = time

            # Free up chairs based on current time
            while leaving_queue and leaving_queue[0][0] <= arrival:
                _, chair = heapq.heappop(leaving_queue)
                heapq.heappush(available_chairs, chair)

            if available_chairs:
                current_chair = heapq.heappop(available_chairs)
            else:
                current_chair = next_chair
                next_chair += 1

            # Push current leave time and chair
            heapq.heappush(leaving_queue, (leave, current_chair))

            # Check if it's the target friend
            if index == targetFriend:
                return current_chair

        return 0