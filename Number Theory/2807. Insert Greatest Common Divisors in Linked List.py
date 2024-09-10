"""
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

Examples:
Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]

Constraints:
The number of nodes in the list is in the range [1, 5000].
1 <= Node.val <= 1000
"""


"""
Intuition: Pretty straightforward simulation problem. Just have to do what is saying. Finding GCD can be done by using built-in gcd() function or by creating new one. As the node will be between two nodes,
we have to ensure there are at least two nodes. Find gcd of their value and create a new node.
Set it to next to the current node and next of this new node will be the previous new node.

Own gcd function:
def _calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
        return a
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head):
        
        cur=head

        while cur.next:
            val=gcd(cur.val,cur.next.val)
            newNode=ListNode(val)
            tmp=cur.next
            cur.next=newNode
            newNode.next=tmp
            cur=tmp
        
        
        return head


