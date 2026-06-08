class AutocompleteSystem:
    
    def trieNode(self):
        dic = defaultdict(lambda:self.trieNode())
        dic["#"] = defaultdict(int)
        return dic
    
    def addWord(self,sentence,count):
        node = self.root
        for char in sentence:
            node = node[char]
            node["#"][sentence]+=count
           
    
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie=lambda:defaultdict(self.trie,{"#":defaultdict(int)})
        self.root=self.trie()
        
        self.query = ""
        for sentence, count in zip(sentences, times):
            self.addWord(sentence,count)


    def input(self, c: str) -> List[str]:
        if c=="#" and len(self.query):
            self.addWord(self.query,1)
            self.query=""
            return []
        else:
            self.query+=c
            node = self.root
            for char in self.query:
                node = node[char]
            ans = heapq.nsmallest(3, node["#"],key = lambda x : (-node["#"][x],x) )
            return ans


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)