class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList: return 0
        n=len(beginWord)

        word_map =defaultdict(list)

        for word in wordList:
            for i in range(n):
                word_map[word[:i]+"*"+word[i+1:]].append(word)

        visited1= defaultdict(int)
        visited2 = defaultdict(int)
        q1=deque([(beginWord,0)])
        q2=deque([(endWord,0)])
        while q1 and q2:
            word,level= q1.popleft()
            if word in visited2:
                return level + visited2[word]+1
          
            visited1[word]=level
            
            for i in range(n):
                for nextword in word_map[word[:i]+"*"+word[i+1:]]:
                    if nextword not in visited1:
                        visited1[nextword] =level+1
                        q1.append((nextword,level+1))

            word,level= q2.popleft()
            if word in visited1:
                return level + visited1[word]+1
            
            visited2[word]=level
            
            for i in range(n):
                for nextword in word_map[word[:i]+"*"+word[i+1:]]:
                    if nextword not in visited2:
                        visited2[nextword]=level+1
                        q2.append((nextword,level+1))


            
        return 0