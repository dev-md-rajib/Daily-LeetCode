"""
Statement: Given an array of integers arr of even length n and an integer k.
We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
Return true If you can find a way to do that or false otherwise.

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
"""

"""
Intuition: The thing matter is what number is required to make a number divisible. We can find it using
modulo operator. Then check if two modulo can full fill each other or not. like if k=5, two modulo are
2 and 3, that means one of them needs 5-2=3 and other one need 5-3=2. As the modulo represents
how much extra it has from last divisible . If they can full fill, means, if there are equal number 
of them to full fill each other then True else False.

Edge case is for modulo 0. As they themself are divisible, we need to just find if they are in even number or not.
"""

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        mem=defaultdict(int)
        
        for num in arr:
            mem[num%k]+=1
            #num % k +k is used in C++, Java and other languages as modulo works differently and return negative number
            #if we modulo negative number. To make it positive, extra k is added.
        if mem[0]%2:
            return False
        for num in range(1,k//2+1):
            if mem[num]!=mem[k-num]:
                return False
  
        return True