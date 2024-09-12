"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4

Constraints:
1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.
"""


"""
Intuition: It's pretty much basic hash set problem. In words, we have to check if a word
contains only the allowed characters. So we iterate over the word and check if each character is 
present in the allowed characters or not. We can brute force over allowed word and try
to find if the current character of word is present or not. A better approach is
to use hash map and store the allowed character. Whenever needed we have to check if the 
current character of the word is in the set or not. We can check it in O(1).
If all the characters are in allowed set, we increase the result.

Advanced Intuition: As we noticed, only unique characters are allowed in "allowed".
So, the max length of it will be 26. In a integer there are at least 32 bits. We can use
a integers bit number as hash index and use as a map. In the first step, we will set 
bit number of the integer according to character number (a-0, b-1 .... z-26) those are allowed.

We then use the integer to check if the current character of word is set in the integer or not.

We can use tracker |= 1<<(characters serial number: ASCII(character)- ASCII('a'))
To check if a bit set in the tracker: (1<<serial_number)&tracker.

"""


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        tracker=0
        for c in allowed:
            val=ord(c)-ord('a')
            tracker |= 1<<val
            print(val,bin(1<<val),bin(tracker))
        res =0

        for word in words:
            res += 1
            for c in word:
                val=ord(c)-ord('a')
                if not (1<<val)&tracker:
                    res -= 1
                    break
        
        return res