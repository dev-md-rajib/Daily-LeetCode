"""
Statement: You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]
"""


"""
Intuition: Overlap for the first time is allowed. Overlapping again in the range which already is overlapped
is not allowed. So, we will create two list to store which are already overlapped and non overlapped. Non overlapped
will be used to create overlapped range while including a new event.
"""

class MyCalendarTwo:

    def __init__(self):
        self.non_overlapping=[]
        self.overlapping=[]

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping:
            if end > s and e > start:
                return False
        
        for s, e in self.non_overlapping:
            if end > s and e > start:
                self.overlapping.append(
                    (max(s,start),min(e,end))
                    )
                
        self.non_overlapping.append((start,end))
        return True


