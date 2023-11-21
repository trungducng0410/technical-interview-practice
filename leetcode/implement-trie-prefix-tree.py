class TrieNode:
    def __init__(self):
        self.isCompletedWord = False
        self.child = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.child:
                trieNode = TrieNode()
                node.child[c] = trieNode
            node = node.child[c]
        node.isCompletedWord = True

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c not in node.child:
                return False
            node = node.child[c]

        return node.isCompletedWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c not in node.child:
                return False
            node = node.child[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
