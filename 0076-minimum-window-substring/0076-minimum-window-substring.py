class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        m,n=len(s),len(t)
        if n>m:return ""
        
        counter=Counter(t)
        count=n

        start=0
        length=inf
        ans_start=None
        for i,char in enumerate(s):
            if char in counter:
                if counter[char]>0:
                    count-=1
                counter[char]-=1
                

                while count==0 and start<=i:
                    if s[start] in counter:
                        counter[s[start]]+=1
                    if  counter[s[start]]>0:
                        count+=1
                    if i-start+1<length:
                        length=i-start+1
                        ans_start=start
                    start+=1

        return "" if length==inf else s[ans_start:ans_start+length]

                    
