"""
Statement: Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

Input: s = "eleetminicoworoep"
Output: 13

Input: s = "leetcodeisgreat"
Output: 5

Input: s = "bcbcbc"
Output: 6
"""

"""
Intuition: We have to find which provides the longest length also having even numbers of
each vowels. Now, only thing matters here is the number of each vowel is even or odd. Does not
matter how many of them are there. Also as there are only 5 vowels, we can keep if they are odd or even
using bit masking. Now when odd numbers of vowel appears, the mask bit corresponding to that vowel
will be set. There are like 2^5 types of combination of odd vowels can make. We can keep track of where
they appear first. Because when they appear again, we can calculate their index difference and find the answer.


Now, the reason why this works because let we found a and e odd numbers of time. Now the mask will
look like this 00011. If we keep traversing and setting bits, and somewhere find bit-mask 00011 again,
that means a and e also odd number of time there. If we remove first appearance of a,e odd numbers of time,
then from the last index to current index, there will be even number of a and e. Because, odd - odd = even.
First appearance represents odd number of a,e . Now if we minus them from current odd a,e then we 
will get even numbers of a,e. 

As this can be applied for any combination of odd bits, we can calculate the longest sub array length.
"""

#solution:

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Dictionary to store the first occurrence of each bitmask state
        seen = {0: -1}
        vowels = 'aeiou'
        mask = 0
        max_len = 0
        
        for i, c in enumerate(s):
            if c in vowels:
                # Toggle the corresponding bit for the vowel
                mask ^= 1 << vowels.index(c)
            
            # If we have seen this bitmask before, calculate the length of the substring
            if mask in seen:
                max_len = max(max_len, i - seen[mask])
            else:
                seen[mask] = i
        
        return max_len
