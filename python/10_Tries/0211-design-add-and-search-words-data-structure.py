"""

211. Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string 
matches any previously added string.

Implement the WordDictionary class:

• WordDictionary() Initializes the object.
• void addWord(word) Adds word to the data structure, it can be matched later.
• bool search(word) Returns true if there is any string in the data structure 
  that matches word or false otherwise. word may contain dots '.' where dots 
  can be matched with any letter.



Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

"""

# Solution 2: Depth First Search (Trie) [✔️]
# Time Complexity: O(n) for addWord(), O(n) for search().
# Space Complexity: O(t + n)

# Where n is the length of the string and t is the total number of TrieNodes created in the Trie.

class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)