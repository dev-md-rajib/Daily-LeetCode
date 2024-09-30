"""
Statement: Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
int pop() Pops and returns the top of the stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.

Input
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
[null,null,null,2,null,null,null,null,null,103,202,201,-1]

Constraints:

1 <= maxSize, x, k <= 1000
0 <= val <= 100
At most 1000 calls will be made to each method of increment, push and pop each separately.
"""

"""
Intuition: Basic implementation.
"""

class CustomStack:

    def __init__(self, maxSize: int):
        self.arr=[]
        self.mx=maxSize

    def push(self, x: int) -> None:
        if len(self.arr)<self.mx:
            self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr):
            x=self.arr.pop()
            return x
        return -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.arr))):
            self.arr[i]+=val


