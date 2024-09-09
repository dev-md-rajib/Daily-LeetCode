"""
Statement: You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

Constraints:

1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000

Example: 
Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]

"""

"""
Initial Intuition: This is simply the simulation as the problem can be solved just 
by doing what the statement wants. Easy linked list traveling too. The grid can be used 
to -1's in a  m x n dimensional grid as the nodes number will be less or equal.

Advanced intuition: Those -1 can be used to keep track if the index is already visited
or not as node value will be always greater than -1.
"""


#Initial solution. Beats 97%.
class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        
        res=[[-1]*n for _ in range(m)]
        #current position in the grid
        c=r=0
        #keep track range using right,bottom, left, up
        right=n
        bottom=m
        left=up=0

        #simulation based 
        while head:
            #go right
            while head and c<right:
                res[r][c]=head.val
                head=head.next
                c+=1
            
            c-=1
            r+=1
            right-=1
            #go down
            while head and r<bottom:
                res[r][c]=head.val
                head=head.next
                r+=1
            
            r-=1
            c-=1
            bottom-=1
            #go left
            while head and c>=left:
                res[r][c]=head.val
                head=head.next
                c-=1
            
            c+=1
            r-=1
            left+=1
            
            #go up
            while head and r>up:
                res[r][c]=head.val
                head=head.next
                r-=1
            r+=1
            c+=1
            up+=1
        return res


#Better written solution:
class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        # Store the east, south, west, north movements in a matrix.
        i = 0
        j = 0
        cur_d = 0
        movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = [[-1 for _ in range(n)] for _ in range(m)]

        while head is not None:
            res[i][j] = head.val
            newi = i + movement[cur_d][0]
            newj = j + movement[cur_d][1]

            if (
                min(newi, newj) < 0
                or newi >= m
                or newj >= n
                or res[newi][newj] != -1
            ):
                cur_d = (cur_d + 1) % 4
            i += movement[cur_d][0]
            j += movement[cur_d][1]

            head = head.next

        return res