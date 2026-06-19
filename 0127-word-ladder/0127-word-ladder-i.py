class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        n=len(beginWord)

        word_map =defaultdict(list)

        for word in wordList:
            for i in range(n):
                word_map[word[:i]+"*"+word[i+1:]].append(word)

        seen=set()
        q=deque([(beginWord,1)])
        while q:
            word,level= q.popleft()
            if word==endWord:return level
            elif word in seen:continue
            seen.add(word)
            for i in range(n):
                for nextword in word_map[word[:i]+"*"+word[i+1:]]:
                    if nextword not in seen:
                        q.append((nextword,level+1))
        return 0