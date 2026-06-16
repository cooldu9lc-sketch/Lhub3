class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s)<=1:return s
        n=len(s)
        counter = Counter(s)
        heap=[(-cnt,s) for s,cnt in counter.items()]
        heapq.heapify(heap)
        print(heap)
        if heap[0][0]*-1 > (n+1)//2 : return ""
        
        res=[]
        while len(heap)>1:
            count1,char1= heapq.heappop(heap)
            count2,char2 =heapq.heappop(heap)
            res+=[char1,char2]
            count1+=1
            count2+=1
            if count1:heapq.heappush(heap, (count1,char1))
            if count2:heapq.heappush(heap, (count2,char2))
        if heap:
            res.append(heapq.heappop(heap)[1])
        return "".join(res)