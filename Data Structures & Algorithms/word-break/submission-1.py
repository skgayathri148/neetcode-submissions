class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True

    def search(self, s, i, j):
        node = self.root
        for idx in range(i, j + 1):
            if s[idx] not in node.children:
                return False
            node = node.children[s[idx]]
        return node.isWord

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        t = 0
        for word in wordDict:
            trie.insert(word)
            t = max(t, len(word))
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s), -1, -1):
            for j in range(i, min(len(s), i + t)):
                if trie.search(s, i, j):
                    dp[i] = dp[j + 1]
                    if dp[i]:
                        break
        
        return dp[0]
        