class Trie:

    def __init__(self):
        self.trie=lambda:defaultdict(self.trie,{"#":0})
        self.root=self.trie()

    def insert(self, word: str) -> None:
        curr=self.root
        for w in word:
            curr=curr[w]
        curr["#"]+=1

    def search(self, word: str) -> bool:
        curr=self.root
        for w in word:
            if w not in curr:
                return False
            curr=curr[w]
        return curr["#"]>=1

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for w in prefix:
            if w not in curr:
                return False
            curr=curr[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)