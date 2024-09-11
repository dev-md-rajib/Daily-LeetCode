"""
Statement: A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

Examples:
Input: start = 10, goal = 7
Output: 3

Input: start = 3, goal = 4
Output: 3

Constraints:
0 <= start, goal <= 109
"""


"""
Intuition: We have to just change the bits where the bits don't match. The larger integer contains extra one's at the left than the smaller one. We have to count that. Using this intuition the problem can be solved using different implementations.

1. Converting numbers to binary then check mis-matches
2. Using AND operation to check the last bit and compare
3. XOR two number and count ones. As the 1's will be at the place of mis match bit.
"""

"""
Learning: Best way to find number of set bits
*** Brian Kernighan’s Algorithm***
Intuition
Brian Kernighan’s algorithm provides an efficient way to count the number of set bits (1s) in an integer by repeatedly eliminating the lowest set bit at each step. The algorithm leverages a clever trick: subtracting 1 from a number flips all the bits after the rightmost 1, including the rightmost 1 itself. When we perform a bitwise AND between the original number and the result of subtracting 1, this operation removes the lowest set bit. This is a nifty observation based on different examples.

Example:
n = 1101100 & n-1 = 1101011 => 1101000 
n = 1101000 & n-1 = 1100111 => 1100000
n = 1100000 & n-1 = 1011111 => 1000000
n = 1000000 & n-1 = 0111111 => 0000000
"""

#Solution -01:
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        return bin(start^goal).count('1')

        st=bin(start)[2:][::-1]
        end=bin(goal)[2:][::-1]
        print(st,end)
        res=0
        for i in range(min(len(st),len(end))):
            if st[i] != end[i]:
                res += 1
        print(res)
        if len(end)>len(st):
            for i in range(len(st),len(end)):
                if end[i]=='1':
                    res+=1
        if len(end)<len(st):
            for i in range(len(end),len(st)):
                if st[i]=='1':
                    res+=1
        return res
    
#Solution -02:
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start > 0 or goal > 0:
            # Increment count if the current bits differ
            if (start & 1) != (goal & 1):
                count += 1
            # Shift both numbers to the right to check the next bits
            #The smaller one will never be negative, it will keep being 0
            start >>= 1
            goal >>= 1
        return count
    
#Solution-03
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #built in function.
        return bin(start^goal).count('1')
    

#Solution-04: Counting set bits using Brian Kernighan’s ALgorithm.
#Taken from LeetCode editorial

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR to find differing bits
        xor_result = start ^ goal
        count = 0
        # Brian Kernighans algorithm to count 1s
        while xor_result:
            xor_result &= xor_result - 1  # Clear the lowest set bit
            count += 1
        return count