"""
Statement: You are given an array words of size n consisting of non-empty strings.

We define the score of a string word as the number of strings words[i] such that word is a prefix of words[i].

For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].

Note that a string is considered as a prefix of itself.

Input: words = ["abc","ab","bc","b"]
Output: [5,4,3,2]
"""

"""
Intuition: It's a basic trie problem. We have to keep a counter at each level and sum them 
while counting for a word. It can be solved also using counting but O(n^3)
"""

#Naive O(n^3)
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        mem=defaultdict(int)
        res=[0]*len(words)
        
        for word in words:
            for sz in range(1,len(word)+1):
                mem[word[:sz]]+=1
        
        for i,word in enumerate(words):
            for sz in range(1,len(word)+1):
                res[i]+=mem[word[:sz]]
        
        return res
        
        
#Trie O(M*N) -official solution for step by step approach

class trie_node:
    def __init__(self):
        self.next = [None] * 26
        self.cnt = 0


class Solution:
    def __init__(self):
        # Initialize the root node of the trie.
        self.root = trie_node()

    # Insert function for the word.
    def insert(self, word):
        node = self.root
        for c in word:
            # If new prefix, create a new trie node.
            if node.next[ord(c) - ord("a")] is None:
                node.next[ord(c) - ord("a")] = trie_node()
            # Increment the count of the current prefix.
            node.next[ord(c) - ord("a")].cnt += 1
            node = node.next[ord(c) - ord("a")]

    # Calculate the prefix count using this function.
    def count(self, s):
        node = self.root
        ans = 0
        # The ans would store the total sum of counts.
        for c in s:
            ans += node.next[ord(c) - ord("a")].cnt
            node = node.next[ord(c) - ord("a")]
        return ans

    def sumPrefixScores(self, words):
        N = len(words)
        # Insert words in trie.
        for i in range(N):
            self.insert(words[i])
        scores = [0] * N
        for i in range(N):
            # Get the count of all prefixes of given string.
            scores[i] = self.count(words[i])
        return scores
