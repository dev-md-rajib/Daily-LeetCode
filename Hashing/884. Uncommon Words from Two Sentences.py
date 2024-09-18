"""
statement: A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
"""

"""
Intuition: We have to just find unique words from the two strings. Words can be found by using
string.split() function and check for unique words.
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s= s1 + " " + s2
        s=s.split(" ")
        counter=Counter(s)
        return [word for word in counter if counter[word]==1]