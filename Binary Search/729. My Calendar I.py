"""
Statement: You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Constraints:

0 <= start < end <= 10^9
At most 1000 calls will be made to book.
"""

"""
Intuition: The problem is straight forward. We to store the previous event times. This can be in many way.
If we store in ordered way, we can use Binary Search to check if anything in that level exists or not.
Normal looping is also accepted as At most 1000 calls will be made.
"""

#Normal Naive way
class MyCalendar:

    def __init__(self):
        self.arr=[]

    def book(self, start: int, end: int) -> bool:
        for u,v in self.arr:
            if u<=start<=v or u<=end-1<=v or start<=u<=end-1 or start<=v<=end-1:
                return False
        
        self.arr.append([start,end-1])
        return True

#Sorted + Binary. Official solution

from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.calendar.bisect_right((start, end))
        if (idx > 0 and self.calendar[idx-1][1] > start) or (idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False
        self.calendar.add((start, end))
        return True