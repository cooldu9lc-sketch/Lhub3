class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        #low keeps tarck of the lowest index of the chars currently in window
        left=res=0
        counter=defaultdict(int)

        for right,char in enumerate(s):
            if char in  counter or len(counter)<2:
                counter[char]+=1
            else:
                while len(counter)==2:
                    counter[s[left]]-=1
                    if counter[s[left]]==0:
                        del counter[s[left]]
                    left+=1
                counter[char]=1

            res=max(res,right-left+1)
        return res