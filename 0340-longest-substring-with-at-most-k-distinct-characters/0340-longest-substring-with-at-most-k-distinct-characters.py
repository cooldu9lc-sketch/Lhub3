class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:return 0
        left=res=0
        counter=defaultdict(int)

        for right,char in enumerate(s):
            if char in  counter or len(counter)<k:
                counter[char]+=1
            else:
                while len(counter)==k:
                    counter[s[left]]-=1
                    if counter[s[left]]==0:
                        del counter[s[left]]
                    left+=1
                counter[char]=1

            res=max(res,right-left+1)
        return res