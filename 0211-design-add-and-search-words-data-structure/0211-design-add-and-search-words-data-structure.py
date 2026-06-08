class WordDictionary:

    def __init__(self):
        self.trie = lambda:defaultdict(self.trie)
        self.root = self.trie()

    def addWord(self, word: str) -> None:
        node=self.root
        for w in word:
            node=node[w]
        node["#"]=True
    
    
    def search(self, word: str) -> bool:
        node=self.root
        i=0
        q=deque([(node,i)])
        while q:
            node,idx=q.popleft()
            if idx==len(word):
                if "#" in node:
                    return True
            elif word[idx]!=".":
                if word[idx] in node:
                    q.append((node[word[idx]],idx+1))
            else:
                for k,v in node.items():
                    if k=="#":continue
                    q.append((v,idx+1))
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)