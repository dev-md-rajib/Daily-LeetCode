"""
Statement: Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]
"""

"""
Intuition: Basic circular queue implementation.
"""

class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.count = 0
        self.front = k - 1
        self.rear = 0
        self.buffer = [0] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.buffer[self.front] = value
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.buffer[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.count -= 1
        return True

    def getFront(self) -> int:
        return self.buffer[(self.front + 1) % self.capacity] if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self.buffer[(self.rear - 1 + self.capacity) % self.capacity] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return not self.count

    def isFull(self) -> bool:
        return self.count == self.capacity

